"""Asks user for a number, goes until they get it right"""


SECRET: int = 4
guess: int = int(input("Guess a number!: "))
playing: bool = True
num_of_guesses: int = 0

while playing:
    num_of_guesses = num_of_guesses + 1
    if num_of_guesses == 2:
        playing = False
    if guess == SECRET:
        print("Yay! You got it right.")
        playing = False
    else:
        print("Wrong number. Try again.")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd")
        if guess > SECRET:
            print("Your guess is too high")
        guess = int(input("Make another guess: "))


