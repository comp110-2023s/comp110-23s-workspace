"""EX02 - one shot wordle """

__author__ = "730575328"

WORD: str = "python"
guess: str = (input("What is your 6-letter guess? "))
playing: bool = True
WHITE_BOX: str = "A"
GREEN_BOX: str = "B"
YELLOW_BOX: str = "C"
count: int = 0
total: int = len(WORD)
emoji: str = ""

while count <= total:
    if guess[count] == WORD[count]:
        emoji + GREEN_BOX
        count = count + 1
    else:
        emoji + WHITE_BOX
        count = count + 1




while playing == True:
    if len(guess) == len(WORD):
        if WORD == guess:
            print(emoji)
            print("Woo! You got it!")
            playing = False
        else:
            print(emoji)
            print("Not quite. Play again soon!")
            playing = False
    else: 
        guess = input("That was not 6 letters! Try again: ")

