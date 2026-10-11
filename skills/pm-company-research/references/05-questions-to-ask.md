# Step 7: Questions to ask the interviewer

"Do you have any questions for us?" is part of the interview. The user usually gets 5 to 7 minutes, about 20% of a first round. Good questions do two jobs at once: they show the homework, and they get the user the signals they named in the intake. Erika Gemzer's example in Lenny's Newsletter is a candidate who mentioned the interviewer's three years at the company and asked how growing privacy regulation had changed their work. It's specific and researched, and it's about the interviewer's own experience.

## The recipe for each question

1. **Start from a signal.** Every question serves one of the user's intake answers ("how long the money lasts", "how much I'd own").
2. **Anchor it in a finding.** Mention what you found in a few words, so the interviewer knows you did the work: "I saw you moved to a subscription model last year…"
3. **Ask about their experience or judgment, not facts on the website.** "How has that changed what the product team works on?" rather than "When did you launch subscriptions?"
4. **Write what to listen for.** A good sign and a warning sign, in a few words. That's how a question turns into a signal.

Shape: *"<finding in ≤ 12 words>. <open question about their experience or view>?"* Keep the spoken question under 20 words, finding included. The page has room for about 16.

## Tag each question by who should get it

Different interviewers can honestly answer different things. Tag each question with the person best placed to answer it:

| Tag | Interviewer | Good ground | Avoid with them |
|---|---|---|---|
| **R** | Recruiter / talent | The process and timeline, why the role is open, team size and structure, how the role is levelled, what made past hires succeed | Deep product strategy |
| **HM** | Hiring manager | What success looks like at 90 days and a year, the biggest problem on the team's plate, how decisions are made and by whom, how they give feedback, what the last person in the role did well or badly | Pay and perks (ask the recruiter) |
| **P** | PM peer | A normal week, how PMs work with engineering and design, where PMs have real say, what's hard about the job, how roadmaps get set | Questions that put them on the spot about their boss |
| **F** | Founder / CEO / exec | Strategy and the next big bet, what they'd stop doing, runway and the next raise or profitability, competition, what they want from product in this phase | Details of day-to-day process |

Aim for a spread: if the user said who they're meeting, give that interviewer type at least 3 questions, and give the others 1 or 2, so the list still works in later rounds. Gemzer's point holds: asking the same good question in more than one round gives you several views on it.

## Sensitive findings: ask neutrally

Layoffs, a down round, a 2.9 on Glassdoor or angry reviews are fair topics if they matter to the user's signals. Ask them as curiosity, not as a gotcha:

- Not: "Why is your Glassdoor rating so low?"
- Better: "I read some reviews about long hours during the last launch. How does the team handle crunch periods now?"
- Not: "Are you going to run out of money?"
- Better (founder or HM): "You raised in early 2025. How are you thinking about the next 18 months: growth, profitability or both?"

## The closing question

End every interview with one closing question. It isn't from Lenny's article; it's a common coaching practice, and it works because it surfaces doubts while the user can still answer them. Pick one and write it for this company:

- "Is there anything about my background that makes you unsure I'd fit this role? I'd like the chance to address it."
- "What would you need to see from me in the next round to feel confident?"
- "If I joined, what would make you say six months from now that it was a great hire?"

The first is the strongest when the user can stay calm hearing a concern. Note in `closing.why` what it does.

## Don't ask

- Anything the website, the JD or your brief already answers.
- Pay, leave or remote policy in a hiring-manager or founder round (save them for the recruiter or the offer stage).
- Yes/no questions.
- Two questions glued together.
- Questions about the interviewer's personal life, even if it's public.

## Output

5 to 7 questions, in the order the user would ask them, each as:
`{ q, who: "R"|"HM"|"P"|"F", why: "<finding> [n]", listen: "<good sign vs warning sign>" }`
plus `closing: { q, why }`. In the .md, also note which signal each question serves.

Sources: Erika Gemzer, Lenny's Newsletter (defining the signals you need, the share of time for your questions, the researched-question example, and reusing questions across rounds). The interviewer-type table, the neutral wording for sensitive findings and the closing question are additions.
