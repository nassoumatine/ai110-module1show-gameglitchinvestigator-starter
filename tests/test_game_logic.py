from logic_utils import check_guess, parse_guess, update_score


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message


def test_guess_too_high():
    # Secret is 50, guess is 60 — should tell the player to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    # Secret is 50, guess is 40 — should tell the player to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_parse_guess_rejects_empty_input():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_rejects_non_numeric_input():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_accepts_decimal_strings():
    ok, value, err = parse_guess("42.0")
    assert ok is True
    assert value == 42
    assert err is None


def test_update_score_win_rewards_fewer_attempts():
    score_after_one_attempt = update_score(0, "Win", 1)
    score_after_three_attempts = update_score(0, "Win", 3)
    assert score_after_one_attempt > score_after_three_attempts


def test_update_score_wrong_guess_does_not_go_negative():
    assert update_score(1, "Too High", 2) == 0
