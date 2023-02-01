"""EX02 - One-Shot Wordle - Loops"""

__author__ = "730556365"

#store the secret word and guess word into variables
secret_word: str = "python"
player_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")

#check if the guess is the correct number of letters
while (len(player_guess) != len(secret_word)):
    player_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

#establish emoji constants
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"



#evaluate the correctness of each letter of the guess word 
#by looping through the indexes of both words and comparing the letters

#green emoji means the guess letter exists in the same index as the secret word
#yellow emoji means the guess letter exists in the secret word but at a different index
#white emoji means the guess letter does not exist in the secret word at all
#emojis are stored in an empty string
idx: int = 0
guess_score: str = ""

while (idx < len(secret_word)):
    contains_char: bool = False
    alt_idx: int = 0
    if (player_guess[idx] == secret_word[idx]):
        guess_score = f"{guess_score}{GREEN_BOX}"
    else:
        while (contains_char == False) and (alt_idx < len(secret_word)):
            if (player_guess[idx] == secret_word[alt_idx]):
                contains_char = True
            else:
                alt_idx = alt_idx + 1
        if (contains_char == True):
            guess_score = f"{guess_score}{YELLOW_BOX}"
        else:
            guess_score = f"{guess_score}{WHITE_BOX}"
    idx = idx + 1
print(guess_score)

#print whether the guess was correct or not
if (player_guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    