"""EX06 - What Taylor Swift Album Are You!"""

def main() -> None:
    "Main function."
    global points
    points = 0
    greet()
    first_question()

points: int 
# tracks adventure points
player: str = input()
# tracks players name


def greet() -> None:
    print("Welcome to the taylor swift quiz! In this quiz, you will figure out what Taylor Swift album you are!")
    name = input("First lets get to know each other, what's your name? ")
    global player 
    player = name 
    return None

def first_question() -> None:
    global points
    print(f'Hi {player}, nice to meet you! In order to prove yourself worthy enough to take this quiz: choose your favorite Taylor Swift album out of these three choices.')
    Answer: str = input("A) Love Story B) Lover C) Midnights (Make sure to answer as A, B, or C and in caps!)")
    if Answer == "A":
        print(f"Thats not even a album, fake fan. Sorry {player} you are out of the quiz! You have {points} adventure point. Better luck next time!")
    elif Answer == "B":
        points += 1
        print(f"Great choice {player}, you pass! You have {points} adventure point, the number of adventure points you earn will determine which album you are!")
    elif Answer == "C":
        points += 2
        print(f"Great choice {player}, you pass! You have {points} adventure point, the number of adventure points you earn will determine which album you are!")


if __name__ == "__main__":    
    main()