import pytest
from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    ai_strategy_helper,
    update_score,
)


def test_get_range_for_difficulty_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_get_range_for_difficulty_normal():
    assert get_range_for_difficulty("Normal") == (1, 100)


def test_get_range_for_difficulty_hard():
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_get_range_for_difficulty_default():
    assert get_range_for_difficulty("SomethingElse") == (1, 100)


def test_parse_guess_valid_integer():
    ok, guess, err = parse_guess("42")
    assert ok is True
    assert guess == 42
    assert err is None


def test_parse_guess_empty_string():
    ok, guess, err = parse_guess("")
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."


def test_parse_guess_none():
    ok, guess, err = parse_guess(None)
    assert ok is False
    assert guess is None
    assert err == "Enter a guess."


def test_parse_guess_invalid_text():
    ok, guess, err = parse_guess("abc")
    assert ok is False
    assert guess is None
    assert err == "That is not a number."


def test_parse_guess_float_string_truncates():
    ok, guess, err = parse_guess("12.9")
    assert ok is True
    assert guess == 12
    assert err is None


def test_check_guess_win():
    outcome, message = check_guess(25, 25)
    assert outcome == "Win"
    assert "Correct" in message


def test_check_guess_too_high():
    outcome, message = check_guess(30, 25)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_too_low():
    outcome, message = check_guess(10, 25)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_ai_strategy_helper_empty_history():
    msg = ai_strategy_helper([], low=1, high=100)
    assert "Start with 50" in msg


def test_ai_strategy_helper_after_too_low():
    history = [{"guess": 30, "outcome": "Too Low"}]
    msg = ai_strategy_helper(history, low=1, high=100)
    assert "Range is now 31 to 100" in msg
    assert "Best next guess: 65" in msg


def test_ai_strategy_helper_after_too_high():
    history = [{"guess": 70, "outcome": "Too High"}]
    msg = ai_strategy_helper(history, low=1, high=100)
    assert "Range is now 1 to 69" in msg
    assert "Best next guess: 35" in msg


def test_ai_strategy_helper_win_history():
    history = [{"guess": 50, "outcome": "Win"}]
    msg = ai_strategy_helper(history, low=1, high=100)
    assert "found the number" in msg


def test_ai_strategy_helper_inconsistent_history():
    history = [
        {"guess": 90, "outcome": "Too Low"},
        {"guess": 80, "outcome": "Too High"},
    ]
    msg = ai_strategy_helper(history, low=1, high=100)
    assert "inconsistent" in msg.lower()


def test_update_score_win():
    assert update_score(0, "Win", 1) == 80


def test_update_score_too_high_even_attempt():
    assert update_score(10, "Too High", 2) == 15


def test_update_score_too_high_odd_attempt():
    assert update_score(10, "Too High", 3) == 5


def test_update_score_too_low():
    assert update_score(10, "Too Low", 2) == 5


def test_update_score_unknown_outcome():
    assert update_score(10, "SomethingElse", 2) == 10