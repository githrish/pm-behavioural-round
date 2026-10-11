# Sources and evidence

The user may repeat a number from this brief to a founder. A wrong valuation or a made-up user count costs them more than a gap does. So: every claim links to its source, every number has a date, and anything derived is marked.

## Evidence tags

| Tag | Means | How it shows on the page |
|---|---|---|
| **Reported** | From the company itself or an official filing (annual report, MCA or SEC filing, exchange filing, company blog, founder on record) | The number, plus [n] |
| **Press** | From a named outlet citing its own reporting or documents | The number, plus [n] |
| **Estimate** | Derived by you or by a source from other numbers | "~" before the number, plus [n] for the inputs; the method goes in the .md |
| **Forum** | Reviews, Reddit, community posts | Used for themes and quotes only, never for company numbers |
| **Not public** | Looked for and not found | The words "Not public", no number |

## Which source wins

1. Official filings and annual reports
2. The company's own statements (press releases, the blog, founders on record)
3. Specialist business press (Entrackr, Inc42, The Morning Context, The Ken, ET Prime, Mint, TechCrunch)
4. Databases (Tracxn, Crunchbase), which are useful for round lists but sometimes lag or merge rounds
5. Forums and reviews, for sentiment only

If two sources disagree, use the higher one on this list, or the more recent one if they're the same level. Put both in the .md under "Conflicts and Gaps".

## Sources by need

| Need | India | Global |
|---|---|---|
| Funding rounds, investors | Tracxn, Entrackr, Inc42, VCCircle, YourStory | Crunchbase, TechCrunch, company press releases |
| Revenue, loss (private) | MCA filings via Entrackr, Inc42, The Morning Context, Tracxn | Reported figures in press; usually not public |
| Revenue, profit (listed) | Screener.in, annual reports, NSE and BSE filings, investor presentations | SEC EDGAR (10-K, S-1), investor relations pages |
| News | Economic Times, Mint, Moneycontrol, Business Standard, Inc42, YourStory | TechCrunch, Bloomberg, Reuters, The Information (headline only) |
| Product numbers | Company posts, founder interviews, Play Store install bands | Company posts, S-1s, press |
| Users' view | Play Store, App Store, Reddit, X | Play Store, App Store, G2, Capterra, Reddit |
| Employees' view | AmbitionBox, Glassdoor | Glassdoor, Blind (headline themes only) |

## Numbers

- Keep the source's currency. Indian figures in ₹ Cr (₹1 Cr = ₹10 million). If you convert, mark it "~", and give the rate and its date in the .md.
- Indian private-company financials are by financial year (FY25 = April 2024 to March 2025). Say which year.
- Install bands ("10M+") are bands, not counts. Write them as shown.
- LinkedIn employee counts drift. Give the date you saw it.

## Runway read (always tagged Estimate)

Most private companies don't disclose cash. Build a careful read from the signals you can find, and say which ones you used:

1. **Cash in:** the last raise (amount and date), plus any reported cash or bank balance from filings.
2. **Burn:** the latest annual loss from filings, or the reported monthly burn. Loss isn't exactly cash burn, so say so.
3. **Arithmetic:** if you have both, months of runway ≈ cash ÷ monthly burn. Show the sum in the .md, e.g. "~$40M raised Mar 2025 ÷ ~$2M a month burn (FY25 loss ₹200 Cr ÷ 12) ≈ ~20 months from the raise, so ~13 months left in Oct 2026".
4. **Signals that change the read:** layoffs, hiring freezes, a bridge or debt round, a down round, a founder saying "profitable" or "default alive", a hiring surge, IPO plans.

On the page, write it in one or two plain sentences, e.g. "Last raise $40M in Mar 2025 [4]. FY25 loss ₹180 Cr [6]. At that burn, roughly 12 to 18 months left, unless they've cut costs. Worth asking." If you don't have the inputs, say what's missing instead of guessing.

## Merge steps

1. Collect every track's findings into one list. Remove duplicates, keeping the best source for each.
2. Number the sources in the order they first appear in the .md, from 1. Use the same numbers on the page.
3. For every number on the page, check that it has a date and a [n]. The build script flags KPIs that don't.
4. Keep source titles short on the page (the build warns if they're cut off). The .md has the full title, publisher, URL, date and tag.
5. List what you couldn't find. Gaps are useful: they're often the best questions to ask.
