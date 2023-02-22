"""EX02 - one shot wordle!"""

__author__ = "730575328"

# defining all my variables 
WORD: str = "python"
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
total: int = len(WORD) 
emoji: str = ""
guess: str = (input(f'What is your {total}-letter guess?'))


while playing is True:
    if len(guess) == len(WORD): 
        if WORD == guess:           # message for if user guesses the secret word
            print("Woo! You got it!")
            playing = False
        else:
            print("Not quite. Play again soon!")
            playing = False         # message for if user guesses the wrong word
    else: 
        guess = input(f'That was not {total} letters! Try again:')  # message for if if the guess is not the same length

while i < total:
    if guess[i] == WORD[i]:
        emoji = emoji + GREEN_BOX   # adds green box to str if the letter is correct and in the right position 
        i = i + 1
    else:
        correct_letters: bool = False 
        alt_index: int = 0    
        while correct_letters is not True and alt_index < total:    # checking through alt. indicies for correct letters in wrong positions
            if WORD[alt_index] == guess[i]:
                correct_letters = True
            else:
                alt_index = alt_index + 1
        if correct_letters is True: 
            emoji = emoji + YELLOW_BOX      # adds yellow box to the str if there is a correct letter in wrong position
            i = i + 1
            alt_index = 0            # initializes alt_index back to original value
            correct_letters = False     # initializes correct_letters back to original value
        else:
            emoji = emoji + WHITE_BOX       # adds white box to the str if the letter is not in the secret word 
            i = i + 1 
            alt_index = 0
            correct_letters = False      
print(emoji)    