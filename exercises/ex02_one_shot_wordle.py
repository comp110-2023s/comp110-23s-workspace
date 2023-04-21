"""EX02 - One - shot Wordle - Loops!"""

__author__ = "730558596"

# This set defines the secret word.
secret_word: str = "python"
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
variable_index: int = 0
guess_emoji: str = ""

# Down below is my defined while loop.
while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")

while variable_index < len(secret_word):
    if guess_word[variable_index] == secret_word[variable_index]:
        guess_emoji = guess_emoji + GREEN_BOX
    
    else:
        letter_exists: bool = False
        alt_index: int = 0 
        while letter_exists is False and alt_index < len(secret_word):
            if guess_word[variable_index] == secret_word[alt_index]:
                letter_exists = bool = True
            else:
                alt_index = alt_index + 1
    
        if letter_exists is True:
            guess_emoji = guess_emoji + YELLOW_BOX
        else:
            guess_emoji = guess_emoji + WHITE_BOX
        
    variable_index = variable_index + 1
print(guess_emoji)

# Defines the results of the loop in refrence to the users word.
if guess_word == secret_word:
    print("Woo! You got it!")

elif len(guess_word) == len(secret_word):
    print("Not quite. Play again soon! ")