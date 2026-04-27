# 🎮 Game Glitch Investigator: The Impossible Guesser

## Title and Summary

This app is the Game Glitch Investigator which runs on Streamlit and is a number guessing game. The original game had a lot of bugs and errors like secret number resetting on every guess or having backwards hints. I fixed those issues and also added an agentic workflow to allow for AI suggestions as to which number would be smarter to guess.

## Architecture Overview

applied-AI-system-gameGlitch/
|-tests/
   |-test_game_logic.py
   |-test_logic_utils.py
|-.gitignore
|-app.py
|-logic_utils.py
|-README.md
|-reflection.md
|-requirements.txt




## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup Instructions

1. Clone the repo, open terminal and run https://github.com/yourusername/applied-AI-System-gameGlitch.git
2. cd applied-AI-System-gameGlitch
3. Install dependencies: `pip install -r requirements.txt`in applied-AI-System-gameGlitch
4. Run the app: `python -m streamlit run app.py` make sure to install streamlit if needed (pip install streamlit)
5. Run tests python -m pytest -v

## Sample Interactions

Input: Difficulty = Easy (1-20), Secret Number = 18
User Guess = 8
Output: Go Higher!
AI Strategist: - Range is now 9 to 19
- Best next guess: 14
- Strategy: You should always guess the middle to minimize attempts

Input: Difficulty = Normal (1-100), Secret Number = 45
User Guess = 45
Output: Correct!
AI Strategist: - Great job! You found the number
- You won! The secret was 17. Final score: 80

Input: Difficulty = Hard (1-500), Secret Number = 145
User Guess = 250
Output: Go Lower!
AI Strategist: - Range is now 144-249
- Best next guess: 197
- Strategy: You should always guess the middle to minimize attempts


## Design Decisions

I separated game logic into logic_utils.py since it easier to test and debug code. The trade-off is that this required more imports and installment and an extra file. I also made the decision to add more difficulty levels (Easy/Normal/Hard) to allow players to select the level they prefer. The trade-off for this was having more edge cases to test. I also wrote unit tests using pytest to validate that each function was running successfully. The trade-off was that I had to install pytest and my test cases would keep failing so it took some time to fix them. I finally made the decision to add a AI strategy helper function which allowed players to think about how to strategically guess the number. The trade-off is that this made the scoring system a bit more complicated.

## Testing Summary

 I managed to get all 28 test cases to pass after fully implementing logic_utils.py. The get_range_for_difficulty() function successfully returns the right ranges for Easy, Normal and Hard Levels. The parse_guess() function handles edge cases, empty strings, non-numeric text and floats. The update_score() function successfully gives the user points for correct guess. The Streamlit app runs successfully without any errors and the secret number does change every new game. 
 
## 📝 Reflection

This project has helped me learn that AI is a benefical tool to debug and find errors in the code. This however can't replace humans critical thinking. When I first ran this game I couldn't guess the secret number because the hints were backwards in which I was guessing numbers that weren't even in the range of the secret number. The biggest lesson is about being able to trust AI because AI can write complex code fast but it is our job to ensure the code is correct and works the way you want it to. I also know that I need to be able to give full context and details to the AI about what I am asking for so the AI can perform the right steps.


