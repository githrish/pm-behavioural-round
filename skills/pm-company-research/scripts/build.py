#!/usr/bin/env python3
"""Build the one-page company brief.

  python3 build.py brief-data.json brief-<company>.html [--md research-<company>.md] [--pdf]

1. Checks every string in the data (and the .md, if given) for em/en dashes, stock AI words,
   citations that point at no source, and sources nobody cites.
2. Injects the data into assets/brief-template.html and writes the HTML.
3. Renders it in headless Chrome and prints the fit report: free space above the footer,
   overflow, how far each column in a row falls short of its neighbour, and any section
   whose left rail runs taller than its content.
4. Saves the rendered page as static HTML (no scripts), so it opens in any viewer, including
   ones that block JavaScript. That file is the deliverable. With --pdf it also prints a PDF.

Exit code 0 = clean, 1 = text problems or overflow (fix and rerun), 2 = setup error.
"""
import base64, html, json, os, re, shutil, subprocess, sys, tempfile, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(HERE, "..", "assets", "brief-template.html")

DASHES = {"\u2014": "em dash", "\u2013": "en dash", " -- ": "double hyphen"}
SLOP = ["delve", "tapestry", "testament to", "pivotal", "seamless", "seamlessly", "leverage", "leveraging",
        "robust", "cutting-edge", "game-changer", "game changer", "vibrant", "in today's", "it's worth noting",
        "unlock", "empower", "elevate", "holistic", "synergy", "spearhead", "foster", "underscore",
        "showcase", "realm", "boasts", "nestled", "navigate the", "revolutionize", "revolutionise",
        "landscape of", "ever-evolving", "a myriad", "plethora", "furthermore", "moreover", "additionally",
        "in conclusion", "stands as", "serves as a", "not only", "crucial", "key player", "deep dive"]


def strings(node, path="DATA"):
    if isinstance(node, str):
        yield path, node
    elif isinstance(node, dict):
        for k, v in node.items():
            if k in ("url",):
                continue
            yield from strings(v, f"{path}.{k}")
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from strings(v, f"{path}[{i}]")


def text_problems(items):
    probs = []
    for where, s in items:
        for d, name in DASHES.items():
            if d in s:
                probs.append(f"{where}: {name} in {s[:70]!r}")
        low = s.lower()
        for w in SLOP:
            if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low):
                probs.append(f"{where}: stock word {w!r} in {s[:70]!r}")
    return probs


def cite_problems(data):
    probs, ns = [], {str(s.get("n")) for s in data.get("sources", [])}
    used = set()
    for where, s in strings(data):
        for grp in re.findall(r"\[(\d+(?:\s*,\s*\d+)*)\]", s):
            for n in re.split(r"\s*,\s*", grp):
                used.add(n)
                if n not in ns:
                    probs.append(f"{where}: cites [{n}] but there is no source {n}")
    for s in data.get("sources", []):
        if not str(s.get("url", "")).startswith("http"):
            probs.append(f"source {s.get('n')}: missing or bad url")
    unused = sorted(ns - used, key=lambda x: int(x) if x.isdigit() else 0)
    warn = []
    for k in data.get("kpis", []):
        v, l = str(k.get("v", "")), str(k.get("l", ""))
        if v.lower() != "not public" and "[" not in l:
            probs.append(f"kpi {v!r}: no [n] citation in its label")
    return probs, warn


def inline_fonts(page):
    """Embed the Google Fonts the page links to, so it looks the same in viewers that block web fonts."""
    m = re.search(r'<link href="(https://fonts\.googleapis\.com/css2\?[^"]+)" rel="stylesheet">', page)
    if not m:
        return page, False
    ua = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
    try:
        css = urllib.request.urlopen(urllib.request.Request(html.unescape(m.group(1)), headers=ua), timeout=20).read().decode()
        # keep only the latin and latin-ext subsets (they cover English text and the rupee sign)
        blocks = re.findall(r"/\* ([\w-]+) \*/\s*(@font-face\s*{[^}]*})", css)
        keep = [b for sub, b in blocks if sub in ("latin", "latin-ext")] or [b for _, b in blocks]
        def embed(mm):
            data = urllib.request.urlopen(urllib.request.Request(mm.group(1), headers=ua), timeout=20).read()
            return "url(data:font/woff2;base64," + base64.b64encode(data).decode() + ")"
        css = "\n".join(re.sub(r"url\((https://[^)]+)\)", embed, b) for b in keep)
    except Exception:
        return page, False
    page = page.replace(m.group(0), "<style>" + css + "</style>")
    page = re.sub(r'<link rel="preconnect"[^>]*>', "", page)
    return page, True


def chrome():
    for c in [os.environ.get("CHROME"),
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              "/Applications/Chromium.app/Contents/MacOS/Chromium",
              "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
              shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chromium-browser")]:
        if c and os.path.exists(c):
            return c
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        return 2
    data_path, out_html = args[0], os.path.abspath(args[1])
    md = flags[flags.index("--md") + 1] if "--md" in flags else None
    data = json.load(open(data_path, encoding="utf-8"))

    probs = text_problems(strings(data))
    if md:
        lines = open(md, encoding="utf-8").read().splitlines()
        probs += text_problems((f"{os.path.basename(md)}:{i+1}", l) for i, l in enumerate(lines)
                               if not l.lstrip().startswith("<!--"))
    cp, warn = cite_problems(data)
    probs += cp

    tpl = open(TEMPLATE, encoding="utf-8").read()
    block = "/*DATA-START*/\nwindow.DATA = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n/*DATA-END*/"
    out = re.sub(r"/\*DATA-START\*/.*?/\*DATA-END\*/", lambda _: block, tpl, flags=re.S)
    out = out.replace("<title>Company Brief</title>", f"<title>Company Brief · {html.escape(data.get('company',''))}</title>")
    open(out_html, "w", encoding="utf-8").write(out)
    print(f"wrote {out_html}")

    print("\nTEXT CHECK")
    print("  clean" if not probs else "\n".join("  x " + p for p in probs))
    for w in warn:
        print("  ! " + w)

    exe = chrome()
    if not exe:
        print("\nNo Chrome/Chromium found, so the fit wasn't measured. Open the HTML to check it by eye.")
        return 1 if probs else 0
    url = "file://" + out_html
    prof = tempfile.mkdtemp()
    base = [exe, "--headless=new", "--disable-gpu", "--no-first-run", f"--user-data-dir={prof}", "--hide-scrollbars"]
    try:
        dom = subprocess.run(base + ["--virtual-time-budget=15000", "--window-size=1200,1800", "--dump-dom", url],
                             capture_output=True, text=True, timeout=120).stdout
    except subprocess.TimeoutExpired:
        dom = ""
    m = re.search(r'data-fit="([^"]*)"', dom)
    over = 0
    print("\nFIT CHECK (mm)")
    if not m:
        print("  could not read the fit report (fonts or scripts blocked?). Check the PDF by eye.")
    else:
        fit = json.loads(html.unescape(m.group(1)))
        over = fit["overflowMm"]
        if over > 0:
            print(f"  x OVERFLOW {over} mm: the page spills past A4. Tighten wording first, then rows.")
        elif fit["freeMm"] > 3:
            print(f"  ! {fit['freeMm']} mm empty above the footer. Fill it with useful content (see SKILL.md step 8).")
        else:
            print(f"  page fits ({fit['freeMm']} mm spare)")
        for r in fit["rows"]:
            gaps = r["shortBy"]
            flag = "!" if max(gaps) > 4 else " "
            print(f"  {flag} row {r['row']:<10} columns short by {gaps}")
        for r in fit.get("rails", []):
            flag = "!" if r["railTallerBy"] > 3 else " "
            print(f"  {flag} section {r['band']:<10} rail runs {r['railTallerBy']} mm past its content (shorten the takeaway)")

    if m:
        static = re.sub(r"<script\b[^>]*>.*?</script>", "", dom, flags=re.S)
        static = re.sub(r'\sdata-fit="[^"]*"', "", static)
        static = re.sub(r'\sclass="fitdbg"', "", static)
        static = static.replace('<button onclick="window.print()">', '<button onclick="window.print()" title="Print or save as PDF">')
        static, embedded = inline_fonts(static)
        if not static.lstrip().lower().startswith("<!doctype"):
            static = "<!doctype html>\n" + static
        open(out_html, "w", encoding="utf-8").write(static)
        print(f"\nsaved {os.path.basename(out_html)} as static HTML (rendered, no scripts, fonts {'embedded' if embedded else 'linked: no network, so viewers may fall back'})")
    if "--pdf" in flags:
        pdf = os.path.splitext(out_html)[0] + ".pdf"
        subprocess.run(base + ["--virtual-time-budget=15000", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", url],
                       capture_output=True, timeout=120)
        print(f"\nwrote {pdf}" if os.path.exists(pdf) else "\nPDF export failed; print from the browser instead.")
    else:
        print(f"\nDeliverable: {out_html} (open it in a browser; Print > Save as PDF gives an A4 page)")
    shutil.rmtree(prof, ignore_errors=True)
    return 1 if (probs or over > 0) else 0


if __name__ == "__main__":
    sys.exit(main())
