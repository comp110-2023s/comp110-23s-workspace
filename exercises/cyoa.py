"""EX06 - Choose Your Own Adventure."""

__author__ = "730556365"

from random import randint

points: int = 0
player: str = ""
num_guesses: int = 0
secret_num: int = randint(1, 20)
num_clues: int = 2

def main() -> None:
    global points, num_guesses, secret_num, num_clues
    greet()
    playing: bool = True

    while num_guesses < 3 and playing is True:
        user_choice: str = input("\nWould you like to get a clue (type '1'), guess the number (type '2'), or end the game (type '3')?: " )
        if user_choice == "1":
            if num_clues > 0:
                get_clue(secret_num)
                num_clues -= 1
            else:
                print("\nYou are out of clues. You must attempt to guess the number.")
        elif user_choice == "2":
            num_guesses += 1
            print(f"\nGuess #{num_guesses}:")
            points = guess_num(points)
        elif user_choice == "3":
            playing = False
        else:
            print("\nInvalid input. Please type 1, 2, or 3.")
    
    print(f"\nGame over, {player}. Your final score is {points}. Good luck next time.")



def greet() -> None:
    global player
    player = input(f"Welcome to Guess The Number! You will have 3 chances to guess a number from 1 to 20. You can ask for two clues per random number.\nWhat is your name?: ")



def get_clue(secret: int) -> None:
    global points
    points -= 5
    print(f"\nPoint Total: {points}")
    clue_choice: str = input("\nWhich type of clue do you want? Type 'even or odd', 'greater than', or 'less than': " )
    while clue_choice != "even or odd" and clue_choice != "greater than" and clue_choice != "less than":
        clue_choice = input(f"\n{clue_choice} is not a valid input. Please try again: ")
    
    if clue_choice == "even or odd":
        if secret % 2 == 0:
            print("\nThe number is even.")
        else:
            print("\nThe number is odd.")
    elif clue_choice == "greater than":
        greater_int: int = int(input("\nType the number you would like to know if the secret number is greater than: "))
        if secret > greater_int:
            print(f"\nThe secret number is greater than {greater_int}")
        else:
            print(f"\nThe secret number is not greater than {greater_int}")
    elif clue_choice == "less than":
        less_int: int = int(input("\nType the number you would like to know if the secret number is less than: "))
        if secret < less_int:
            print(f"\nThe secret number is less than {less_int}")
        else:
            print(f"\nThe secret number is not less than {less_int}")


        
def guess_num(points: int) -> int:
    global secret_num, num_guesses, num_clues
    player_guess = int(input("\nWhat do you think the secret number is?: "))
    
    if player_guess == secret_num:
        points += 50
        print(f"\nCorrect. The secret number is {secret_num}.\nPoint Total: {points}")
        num_guesses = 0
        num_clues = 2
        secret_num = randint(1, 20)
    else:
        print(f"\nWrong. The secret number is not {player_guess}.")

    return points



if __name__ == "__main__":
    main()