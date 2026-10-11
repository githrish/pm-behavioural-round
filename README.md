# PM Interview Skills

Claude skills that prepare product managers for first-round interviews. They're built on Coach Erika Gemzer's MVIP (Minimum Viable Interview Prep) framework from Lenny's Newsletter: [How to pass any first-round interview](https://www.lennysnewsletter.com/p/how-to-pass-any-first-round-interview).

The series has three skills, each run at a different time:

| # | Skill | When | Status |
|---|---|---|---|
| 1 | **pm-story-bank** | Once per job search | Ready |
| 2 | **pm-company-research** | Once per company | Ready |
| 3 | Role tailoring + mock interview | Once per interview | Coming soon |

## Skill 1: pm-story-bank

It turns your resume, plus any prep notes or docs you have, into a story bank you can reuse across interviews:

- **Your top 3 stories in STAR++:** Situation, Task, Action, Result, plus Learnings and Future improvements. The skill ranks every story on your resume, you pick three, and it asks at most 5 questions per story to fill the gaps.
- **"Tell me about yourself"** as a timed outline built on one thread, not a walk through your resume.
- **Your reasons:** why now, why PM, and any gaps on your resume.
- **A question map** covering Lenny's three question types. Pure ("Tell me about a time…") questions map to a story. Theoretical ("How do you…?") questions get principles plus a proof story. Situational ("What would you do if…?") questions get your first moves.
- **Career switchers** moving into PM from sales, GTM, marketing, engineering and other roles get their experience reframed in PM language, without overclaiming.

**Output:**
- **A portrait A4 PDF pack:** an overview and question map, then one page per story. Each story page has the spoken script, the 30-second version, the call you made, the numbers, and likely follow-ups.
- **`story-bank.md`:** the full record, which the later skills read.

## Skill 2: pm-company-research

Give it a company name, plus the role and JD if you have them. It researches the company and writes the questions you'll ask the interviewer:

- **Your signals first.** Following Lenny's approach, it asks what you need to find out to decide whether you want the job, and every question it writes serves one of those answers. It asks at most 3 questions before it starts researching.
- **Parallel research** on the company and business model, founders and what they've said publicly, funding, valuation and runway, product numbers, user flows, funnel and monetisation, competitors, and sentiment from the Play Store, App Store, G2, Glassdoor, AmbitionBox and Reddit. It uses Indian sources (Tracxn, Inc42, Entrackr, YourStory, Screener.in) where they fit.
- **Every claim is sourced.** Numbers carry a date and a [n] link, estimates are marked "~" with the method, and anything it can't find says "Not public".
- **An optional product walkthrough.** You sign in yourself; it browses read-only and notes the persona, funnel, money moments and friction.
- **5 to 7 questions** tagged by interviewer type (recruiter, hiring manager, peer, founder), each with what to listen for, plus a closing question.

**Output:**
- **A one-page A4 brief (HTML):** key numbers, then numbered sections for the business, leadership, funding and runway, the product funnel, competitors, sentiment and your questions, each with a one-line takeaway. Print it to PDF from the browser if you want one.
- **`research-<company>.md`:** the full record with every source link, which Skill 3 reads alongside `story-bank.md`. If you've built a story bank, the talking points link to your stories.

## Install

**Claude Code:** copy the skill folder into your skills directory.

```bash
git clone https://github.com/githrish/pm-behavioural-round.git
cp -R pm-behavioural-round/skills/pm-story-bank ~/.claude/skills/
cp -R pm-behavioural-round/skills/pm-company-research ~/.claude/skills/
```

**Claude.ai:** download `dist/pm-story-bank.skill` and `dist/pm-company-research.skill`, and upload them under Settings → Capabilities → Skills.

Then say something like: *"Help me build my PM story bank. Here's my resume."* or *"I have a PM interview at Zepto next week. Research the company."*

The company brief is built by `scripts/build.py`, which checks the text and uses headless Chrome to check the one-page fit.

## Credit and sources

**The foundation** is Coach Erika Gemzer's guest post on Lenny's Newsletter, [How to pass any first-round interview (even in a terrible talent market)](https://www.lennysnewsletter.com/p/how-to-pass-any-first-round-interview) (July 2023). From it, these skills take:
- MVIP (Minimum Viable Interview Prep), the idea of minimum prep that still works
- the career story and having one decisive reason for wanting the role
- "walking down memory lane": 3 to 5 big, recent projects instead of hundreds of scripted answers
- STAR++: STAR plus Learnings and Future improvements
- the pure / theoretical / situational question split and how to answer each
- defining the signals you need to decide whether you want the role, researching the company, competitors and interviewers, and the share of the interview that goes to your own questions (Skill 2)
- mirroring the job description's language, which comes in Skill 3

The skills paraphrase the article; they don't reproduce it. Read the original. It's worth it.

**Additions** that aren't in the article come from further research:
- "Tell me about yourself": Aakash Gupta, Product Growth ([tell me about yourself](https://www.news.aakashg.com/p/go-from-410-to-1010-on-tell-me-about), [first-round questions](https://www.aakashg.com/first-round-interview-questions/)); Joel Schwartzberg in HBR, via [Cornell's summary](https://hecec.human.cornell.edu/2021/11/02/6907/); [Exponent](https://www.aced.io/blog/prepare-product-management-behavioral-interviews); [NextLevel Coach](https://www.nextlevel.coach/blog/tell-me-about-yourself-career-change)
- Stories and judgment: Jackie Bavaro, [Use PEARL instead of STAR](https://jackiebavaro.substack.com/p/use-pearl-instead-of-star-to-shine); [Amazon's interview guidance](https://amazon.jobs/en-gb/landing_pages/in-person-interview); Exponent's leadership and drive rubric; Lewis Lin, *Decode and Conquer*
- Career switchers: [Product Leadership](https://www.productleadership.com/sales-to-product-manager/), [Earlywork](https://earlywork.substack.com/p/-from-marketing-to-product), [freeCodeCamp](https://www.freecodecamp.org/news/how-to-land-a-pm-job-without-pm-experience/)
- Indian PM hiring: [Jobrise](https://jobrise.io/blog/flipkart-meesho-zomato-interview-india), [Razorpay on how it hires PMs](https://razorpay.com/unfiltered/how-we-hire-product-managers-and-what-to-expect-in-your-pm-interviews-at-razorpay/)

- Company research (Skill 2): tagging questions by interviewer type, the closing question, the evidence tags (Reported, Press, Estimate, Forum) and the India source list are additions, not from the article.

Each reference file in `skills/pm-story-bank/references/` ends with its own sources line.

This project isn't affiliated with or endorsed by Lenny's Newsletter or Erika Gemzer.

## License

MIT. See [LICENSE](LICENSE).
