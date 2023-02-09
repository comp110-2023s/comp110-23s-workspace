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