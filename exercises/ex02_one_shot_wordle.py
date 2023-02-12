"""EX02 - one shot wordle """

__author__ = "730575328"

WORD: str = "python"
playing: bool = True
WHITE_BOX: str = "W"
GREEN_BOX: str = "G"
YELLOW_BOX: str = "Y"
count: int = 0
total: int = len(WORD) 
emoji: str = ""
guess: str = (input(f'What is your {total}-letter guess?'))

while playing == True:
    if len(guess) == len(WORD):
        if WORD == guess:
            print("Woo! You got it!")
            playing = False
        else:
            print("Not quite. Play again soon!")
            playing = False
    else: 
        guess = input(f'That was not {total} letters! Try again:')

while count < total:
    if guess[count] == WORD[count]:
        emoji = emoji + GREEN_BOX
        count = count + 1
    else:
        correct_letters: bool = False 
        alternate_indices: int = 0
        while correct_letters == False and alternate_indices < total:
            if guess[alternate_indices] == WORD[count]:
                emoji = emoji + YELLOW_BOX
                correct_letters = True
            else:
                alternate_indices = alternate_indices + 1
    # else:
    #     emoji = emoji + WHITE_BOX
    #     count = count + 1
print(emoji)


# while correct_letters and alternate_indices < total:
#          if WORD[alternate_indices] == WORD[count]:
#             corect_letters = False
#             emoji = emoji + YELLOW_BOX
#          else:
#             alternate_indices = alternate_indices + 1

