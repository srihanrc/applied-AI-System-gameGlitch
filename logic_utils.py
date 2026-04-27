def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "� Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        g = str(guess)
        s = str(secret)
        if g == s:
            return "Win", "🎉 Correct!"
        if g > s:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

def ai_strategy_helper(history, low=1, high=100):
    current_low = low
    current_high = high

    if not history:
        midpoint = (current_low + current_high) // 2
        return f"AI Strategy Helper: Start with {midpoint}. This cuts the range in half."

    for item in history:
        if not isinstance(item, dict):
            continue

        guess = item.get("guess")
        outcome = item.get("outcome")

        if outcome == "Too Low":
            current_low = max(current_low, guess + 1)
        elif outcome == "Too High":
            current_high = min(current_high, guess - 1)
        elif outcome == "Win":
            return "AI Strategy Helper: Great job! You found the number."

    if current_low > current_high:
        return "AI Strategy Helper: The hints seem inconsistent. Something may be glitched."

    best_next_guess = (current_low + current_high) // 2


    return (
        f"AI Strategy Helper:\n"
        f"- Range is now {current_low} to {current_high}\n"
        f"- Best next guess: {best_next_guess}\n"
        f"- Strategy: You should always guess the middle to minimize attempts.\n"
    )
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
