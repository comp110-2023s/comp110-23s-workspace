"""EX02 - one shot wordle """

__author__ = "730575328"

WORD: str = "python"
guess: str = (input("What is your 6-letter guess? "))
playing: bool = True
WHITE_BOX: str = "A"
GREEN_BOX: str = "B"
YELLOW_BOX: str = "C"
count: int = 0
emoji: str = ""

while len(emoji) <= len(WORD):
    if guess[count] == WORD[count]:
        print(emoji + GREEN_BOX)
        count = count + 1
    else:
        print(emoji + GREEN_BOX)
        count = count + 1


while playing == True:
    if len(guess) == len(WORD):
        if WORD == guess:
            print("Woo! You got it!")
            playing = False
        else:
            print("Not quite. Play again soon!")
            playing = False
    else: 
        guess = input("That was not 6 letters! Try again: ")

