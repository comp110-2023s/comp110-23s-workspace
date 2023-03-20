"""EX06 - Choose Your Own Adventure."""

__author__ = "730556365"

from random import randint

points: int = 0
player: str = ""
num_guesses: int = 0
secret_num: int = randint(1, 70)
num_clues: int = 2


def main() -> None:
    """Function runs the main game loop."""
    global points, num_guesses, secret_num, num_clues
    greet()
    playing: bool = True

    while num_guesses < 3 and playing is True:
        user_choice: str = input(f"\nWhat would you like to do, {player}?\nTo get a clue, type '1'... To guess the number, type '2'... To end the game, type '3': ")
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
        print(f"\nPoint Total: {points}")
    
    print(f"\nGame over, {player}. Your final score is {points}. Good luck next time.")


def greet() -> None:
    """Function greets the player and collects the player's name."""
    global player
    player = input("Welcome to Guess The Number! You will have 3 chances to guess a number from 1 to 70. You can ask for two clues per random number.\nWhat is your name?: ")


def get_clue(secret: int) -> None:
    """Function gives the player a clue of their choice and subtracts a number of points depending on the chosen clue."""
    global points, player
    clue_choice: str = input(f"\nWhich type of clue do you want, {player}? Type 'even or odd', 'greater than', or 'sum of digits': ")

    while clue_choice != "even or odd" and clue_choice != "greater than" and clue_choice != "sum of digits":
        clue_choice = input(f"\n'{clue_choice}' is not a valid input, {player}. Please try again: ")
    
    if clue_choice == "even or odd":
        print(even_or_odd(secret))
        points -= 5
    elif clue_choice == "greater than":
        print(greater_than(secret))
        points -= 5
    elif clue_choice == "sum of digits":
        print(sum_of_digits(secret))
        points -= 15


def even_or_odd(secret: int) -> str:
    """Function determines if a number is even or odd."""
    if secret % 2 == 0:
        return "\nThe number is even."
    else:
        return "\nThe number is odd."


def greater_than(secret: int) -> str:
    """Function determines if one number is greater than another."""
    greater_int: int = int(input("\nType the number you would like to know if the secret number is greater than: "))
    if secret > greater_int:
        return f"\nThe secret number is greater than {greater_int}"
    else:
        return f"\nThe secret number is not greater than {greater_int}"


def sum_of_digits(secret: int) -> str:
    """Function sums the digits of a number."""
    digit_sum: int = 0
    for digit in str(secret): 
        digit_sum += int(digit)      
    return f"\nThe sum of the secret number's digits is {digit_sum}"

        
def guess_num(points: int) -> int:
    """Function asks the player to guess a number and tells the player if they are correct."""
    global secret_num, num_guesses, num_clues, player
    CHECK_MARK_EMOJI: str = "\U00002705"
    RED_X_EMOJI: str = "\U0000274C"
    player_guess = int(input("\nWhat do you think the secret number is?: "))
    
    if player_guess == secret_num:
        points += 100
        print(f"\nThat's correct, {player}!!{CHECK_MARK_EMOJI}{CHECK_MARK_EMOJI}. The secret number is {secret_num}.")
        num_guesses = 0
        num_clues = 2
        secret_num = randint(1, 70)
    else:
        points -= 2
        print(f"\nThat's wrong, Connor. {RED_X_EMOJI} The secret number is not {player_guess}.")

    return points


if __name__ == "__main__":
    main()