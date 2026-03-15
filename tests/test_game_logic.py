from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

def test_check_guess_string_secret():
    # Test when guess is int and secret is str (even attempts)
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_check_guess_guess_str_secret_int():
    # Test when guess is str and secret is int (odd attempts)
    outcome, message = check_guess("60", 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_check_guess_guess_str_secret_str():
    # Test when both are str
    outcome, message = check_guess("40", "50")
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
