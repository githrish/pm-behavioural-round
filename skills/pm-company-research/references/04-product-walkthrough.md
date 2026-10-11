# Step 4: Product walkthrough

Interviewers notice when a candidate has actually used the product. "I signed up and it took four screens before I saw a single item" beats any number from a press release. This step gets the user as close to that as possible without you ever handling their login.

Ask once, after the research subagents have started (so it doesn't hold anything up). Use the question tool:

"Want me to walk through <product> logged in? You'd sign in yourself in the browser, and I'd look around read-only: no purchases, posts or settings changes."
Options: "Yes, I'm already signed in in Chrome", "Yes, I'll sign in in the browser pane", "No, public pages only", "It's app-only, give me the checklist".

## Mode 1: logged-in walkthrough (the user opted in)

- **The user signs in, never you.** With Claude in Chrome, use their existing session. With the built-in browser, open the login page and ask them to sign in in the pane, then wait until they say they're done. Never type a password, create an account, or accept terms for them.
- **Read-only.** Look, scroll and open menus. Don't buy, add payment details, send messages, post, invite, rate, change settings, or submit any form. If a step needs one of those to go further, stop there and note it. That is useful in itself ("the paywall hits before any free value").
- **Stay in the product.** Don't open the user's personal data beyond what you need to see the flow (e.g. don't read their messages or orders in detail), and never copy their name, phone number or address into the brief.
- **Don't change their state.** Adding to cart, saving or following changes the user's account, so skip it. Most of what you need (prices, fees, thresholds, offers) shows without it.
- **What to capture:**
  - **Persona signals:** what onboarding asks, the defaults, the copy's tone, and who it seems built for.
  - **Time to first value:** how many screens or steps until something useful happens.
  - **The core loop:** what a user does repeatedly, and what brings them back (notifications, streaks, saved items).
  - **The money moments:** where the product asks for money or shows ads, and the plans and prices shown (with the date).
  - **Friction:** long forms, permission asks, dead ends, confusing labels, slow screens.
  - **Thresholds and nudges:** free-delivery minimums, "add ₹X more" bars, offer or reward ladders, and membership prompts. These are often where the growth strategy shows, and you can see them without adding anything to the cart.
  - **Something good:** one thing that's better than competitors. You'll want something positive to say in the interview.
- Note the method as "logged-in web walkthrough, <date>" in the .md and on the page (`product.method`).

## Mode 2: public pages (default if no login)

Browse the homepage, pricing page, signup page (without submitting), help centre or docs, and the store listings (screenshots and "what's new" notes). Help docs are underrated: they describe flows step by step. Method: "public site, pricing, help docs and store listing, <date>".

## Mode 3: app-only products, the 10-minute checklist

You can't drive a phone app, so give the user this checklist to do themselves, and offer to fold their notes into the brief if they paste them back:

1. Install and open it. Count the screens before you see anything useful.
2. What does onboarding ask you? What does that tell you about who they're targeting?
3. Do the one core thing the app is for (search, order, pay, book, learn). Where did you hesitate?
4. Where does it ask for money, and how much? Is there a free tier, trial or first-order offer?
5. What notification or permission does it ask for, and when?
6. Find one thing you'd fix and one thing you'd steal for another product.
7. Open the top competitor and do the same core task. Which was faster?

Until they do, build the flows from the store screenshots, help docs and reviews, and set the method to "store listing, help docs and reviews (not used first-hand)".

## How it shows in the brief

- `product.funnel`: 4 to 6 steps, first visit to repeat use, with `money: true` on the step that makes money.
- `product.persona`: one or two sentences.
- `product.notice`: 3 or 4 specific observations, at least one of them positive. These are what the user says when asked "What do you think of our product?"
