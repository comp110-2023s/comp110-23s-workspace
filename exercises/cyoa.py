"""EX06 - Choose Your Own Adventure."""

__author__ = "730556365"


points: int = 0
player: str = ""

from random import randint

def main() -> None:
    global points
    greet()
    secret_num: int = randint(0, 10)
    num_guesses: int = 0
    playing: bool = True

    while num_guesses < 3 and playing is True:
        user_choice: str = input("Would you like to get a clue (type '1'), guess the number (type '2'), or end the game (type '3')?: " )
        if user_choice == "1":
            get_clue(secret_num)
        elif user_choice == "2":
            num_guesses += 1
            print(f"Guess #{num_guesses}:")
            points = guess_num(points, secret_num)
        elif user_choice == "3":
            print(f"Game over, {player}. Your final score is {points}. Good luck next time.")
            playing = False
        else:
            print("Invalid input. Please type 1, 2, or 3.")


def greet() -> None:
    global player
    player = input(f"Welcome to Guess The Number! You will have 3 chances to guess a number from 1 to 10. You can ask for one clue per random number. What is your name?: ")


def get_clue(secret_num: int) -> None:
    global points
    points -= 5
    clue_choice: str = input("Which type of clue do you want? Type 'even or odd', 'greater than', or 'less than': " )
    
    if clue_choice == "even or odd":
        if secret_num % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")
    elif clue_choice == "greater than":
        greater_int: int = int(input("Type the number you would like to know if the secret number is greater than: "))
        if secret_num > greater_int:
            print(f"The secret number is greater than {greater_int}")
        else:
            print(f"The secret number is not greater than {greater_int}")
    elif clue_choice == "less than":
        less_int: int = int(input("Type the number you would like to know if the secret number is greater than: "))
        if secret_num < less_int:
            print(f"The secret number is less than {less_int}")
        else:
            print(f"The secret number is not less than {less_int}")


        
def guess_num(points: int, secret_num: int) -> int:
    player_guess = int(input("What do you think the secret number is?: "))
    
    if player_guess == secret_num:
        print(f"Correct. The secret number is {secret_num}.")
        points += 50
    else:
        print(f"Wrong. The secret number is not {player_guess}")

    return points







if __name__ == "__main__":
    main()