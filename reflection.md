# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game loaded in Streamlit with a sidebar for difficulty, a guess input, and a Developer Debug Info panel. It looked playable at first glance, but once I started submitting guesses the hints did not match the secret number and the score changed in confusing ways.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The hints were backwards — when my guess was too high, the game told me to go higher instead of lower. The secret number was sometimes converted to a string on even-numbered attempts, which caused wrong comparisons. The New Game button did not fully reset the session, so I had to refresh the browser to play again. The info banner always said "1 and 100" even when I picked Easy or Hard.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|------------|-------------------|-----------------|------------------------|
| Guess 60 (secret 50) | "Too High" / Go LOWER | "Too High" / Go HIGHER | none |
| Guess 40 (secret 50) | "Too Low" / Go HIGHER | "Too Low" / Go LOWER | none |
| Click New Game after winning | Fresh game, score 0, status playing | Still showed "You already won" until browser refresh | none |
| Easy difficulty selected | Banner shows range 1–20 | Banner always showed 1–100 | none |
| 2nd guess in same round | Compare guess to int secret | Secret coerced to string on even attempts | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used an in-editor AI coding assistant in VS Code to read `app.py` and `logic_utils.py`, explain the buggy logic, and help refactor functions into `logic_utils.py`.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI pointed out that `check_guess` returned "Go HIGHER!" when `guess > secret`, which is backwards. It suggested swapping the hint messages so a high guess tells the player to go lower. I moved the fixed function into `logic_utils.py` and confirmed with pytest that `check_guess(60, 50)` returns `"Too High"` with a LOWER message.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  At one point the AI suggested removing the Developer Debug Info panel entirely so players would not see the secret. I rejected that because the panel is useful for debugging during development; the real bug was the hint logic and session state, not the panel itself. I kept the panel and verified the actual fixes by playing the game and running tests instead.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I checked each fix two ways: first with targeted pytest cases for the logic functions, then by running the Streamlit app and replaying the same inputs from my bug log. A fix counted as done only when both the automated test and the live game behaved as expected.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I added `test_guess_too_high`, which calls `check_guess(60, 50)` and asserts the outcome is `"Too High"` with a LOWER hint. Before the fix this test failed because the message said HIGHER. After the fix, all eight tests passed, which gave me confidence the core comparison logic was correct.

- Did AI help you design or understand any tests? How?
  Yes. I asked the AI to suggest edge cases like empty input, non-numeric strings, and decimal values like `"42.0"`. It generated pytest cases for `parse_guess` and a score floor test for `update_score`, which helped me verify input validation and scoring without manually clicking through every scenario.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns your entire script from top to bottom every time you interact with the page, like clicking a button. That means regular variables reset unless you store them in `st.session_state`, which persists values across reruns. Once I understood that, it was clear why the New Game button had to reset every session key — not just the secret number — or the UI would stay stuck in a won/lost state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  Writing a small bug reproduction table before fixing anything. Listing the input, expected result, and actual result kept me focused and made it easy to turn each bug into a pytest case later.

- What is one thing you would do differently next time you work with AI on a coding task?
  I would tackle one bug per chat session from the start. When I tried to fix everything in one big prompt early on, the suggestions were harder to review. Smaller, targeted prompts with a specific file attached worked much better.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  AI-generated code can look finished even when the logic is subtly wrong, so I now treat it as a draft that needs tests and manual verification. The AI is helpful for spotting patterns quickly, but I still need to read the diff and run the game myself before trusting a fix.
