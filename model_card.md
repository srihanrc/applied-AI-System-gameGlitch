# 💭 Reflection: Game Glitch Investigator
---

## Debugging and testing your fixes

At first I only had 14 out of 28 cases pass because I had missed context in 2 of my functions. After implementing the code for those functions the accuracy drastically improved and I had 28 out of 28 test cases pass with also no errors in streamlit app. 

## Reflection

Some limitations and biases of this system is that this can only handle integer guesses within the guessing range and it's not able to handle edge cases like non-numeric input or numbers outside guessing range. AI could be misused if someone just copied code and put it as production ready without verifying to see if the code actually works. The previous version had errors where the hints were backwards so to avoid this I would ask the AI assistant to fix these bugs and making sure I review the changes before deploying. When testing the AI's reliabilty, I was surprised how AI had confidently suggested bug fixes which led to other bugs for example AI recommending a scoring formula which didn't account for negative values in which the pytest case failed because of that. AI was helpful when it gave me an idea as to how to write my agent workflow code and also gave me good test cases to make sure my functions were working well. This was flawed because once the user won the game it was stuck in the Congrats you win state so the AI helper wasn't giving hints at the start of the next game.
