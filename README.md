# PM Interview Skills

Claude skills that prepare product managers for first-round interviews. They're built on Coach Erika Gemzer's MVIP (Minimum Viable Interview Prep) framework from Lenny's Newsletter: [How to pass any first-round interview](https://www.lennysnewsletter.com/p/how-to-pass-any-first-round-interview).

The series has three skills, each run at a different time:

| # | Skill | When | Status |
|---|---|---|---|
| 1 | **pm-story-bank** | Once per job search | Ready |
| 2 | pm-company-research | Once per company | Coming soon |
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

## Install

**Claude Code:** copy the skill folder into your skills directory.

```bash
git clone https://github.com/githrish/pm-behavioural-round.git
cp -R pm-behavioural-round/skills/pm-story-bank ~/.claude/skills/
```

**Claude.ai:** download `dist/pm-story-bank.skill` and upload it under Settings → Capabilities → Skills.

Then say something like: *"Help me build my PM story bank. Here's my resume."*

## Credit

The framework is from Erika Gemzer's guest post on Lenny's Newsletter (July 2023). These skills paraphrase and extend it, with additional research on "Tell me about yourself" and PM behavioral interviews. They aren't affiliated with Lenny's Newsletter.

## License

MIT. See [LICENSE](LICENSE).
