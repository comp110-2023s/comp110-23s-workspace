"""Ask user for number, give hints abt numbe if wrong"""

SECRET: int = 10
guess: int = int(input("Guess a number! "))
playing: bool = True

while playing:
    if guess == SECRET:
        print("correct")
# while playing:
#     if guess == SECRET:
#         print("Correct! You did it! Believe in your dreams <3")
#         playing = False
#     else: 
#         guess = int(input("Wrong guess try again"))

# to comment out multiple lines then use ctrl /
WHITE_BOX: str = "W"
GREEN_BOX: str = "G"
YELLOW_BOX: str = "Y"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"