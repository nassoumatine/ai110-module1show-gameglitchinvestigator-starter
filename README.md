# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  This is a number-guessing game built with Streamlit. The player picks a difficulty, enters guesses within a range, and tries to find the secret number before running out of attempts.

- [x] Detail which bugs you found.
  Reversed high/low hints, secret coerced to string on even attempts, incorrect attempts-left counter, hardcoded range in the info banner, broken New Game reset, and unpredictable score changes.

- [x] Explain what fixes you applied.
  Moved core logic into `logic_utils.py`, corrected hint directions, kept the secret as an integer, reset all session state on New Game, fixed the range banner, and simplified scoring so wrong guesses deduct 2 points and wins reward fewer attempts.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User opens the app and selects **Normal** difficulty (range 1–100, 8 attempts).
2. User enters a guess of **40** → game shows **"Too Low"** with hint **"Go HIGHER!"**
3. User enters **70** → game shows **"Too High"** with hint **"Go LOWER!"**
4. Score decreases by 2 after each wrong guess and stays visible in Developer Debug Info.
5. User enters the correct secret number → balloons appear, status changes to won, and final score is displayed.
6. User clicks **New Game** → attempts, score, history, and status all reset without refreshing the browser.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
============================= test session starts ==============================
platform darwin -- Python 3.12.4, pytest-9.0.3, pluggy-1.6.0
collected 8 items

tests/test_game_logic.py::test_winning_guess PASSED                      [ 12%]
tests/test_game_logic.py::test_guess_too_high PASSED                     [ 25%]
tests/test_game_logic.py::test_guess_too_low PASSED                      [ 37%]
tests/test_game_logic.py::test_parse_guess_rejects_empty_input PASSED    [ 50%]
tests/test_game_logic.py::test_parse_guess_rejects_non_numeric_input PASSED [ 62%]
tests/test_game_logic.py::test_parse_guess_accepts_decimal_strings PASSED [ 75%]
tests/test_game_logic.py::test_update_score_win_rewards_fewer_attempts PASSED [ 87%]
tests/test_game_logic.py::test_update_score_wrong_guess_does_not_go_negative PASSED [100%]

============================== 8 passed in 0.01s ===============================
```

Run locally with: `pytest tests/ -v`

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
