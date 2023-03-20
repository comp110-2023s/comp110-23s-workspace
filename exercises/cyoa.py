"""EX06 - Choose Your Own Adventure."""

__author__ = "730556365"

from random import randint

points: int = 0
player: str = ""
num_guesses: int = 0
secret_num: int = randint(1, 70)
num_clues: int = 2

def main() -> None:
    global points, num_guesses, secret_num, num_clues
    greet()
    playing: bool = True

    while num_guesses < 3 and playing is True:
        user_choice: str = input(f"\nWhat would you like to do, {player}?\nTo get a clue, type '1'... To guess the number, type '2'... To end the game, type '3': " )
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
    player = input(f"Welcome to Guess The Number! You will have 3 chances to guess a number from 1 to 70. You can ask for two clues per random number.\nWhat is your name?: ")



def get_clue(secret: int) -> None:
    global points, player
    clue_choice: str = input(f"\nWhich type of clue do you want, {player}? Type 'even or odd', 'greater than', or 'sum of digits': " )

    while clue_choice != "even or odd" and clue_choice != "greater than" and clue_choice != "sum of digits":
        clue_choice = input(f"\n'{clue_choice}' is not a valid input, {player}. Please try again: ")
    
    if clue_choice == "even or odd":
        print(even_or_odd(secret))
        points -= 5
        print(f"\nPoint Total: {points}")
    elif clue_choice == "greater than":
        print(greater_than(secret))
        points -= 5
        print(f"\nPoint Total: {points}")
    elif clue_choice == "sum of digits":
        print(sum_of_digits(secret))
        points -= 15
        print(f"\nPoint Total: {points}")



def even_or_odd(secret: int) -> str:
    if secret % 2 == 0:
        return "\nThe number is even."
    else:
        return "\nThe number is odd."



def greater_than(secret: int) -> str:
    greater_int: int = int(input("\nType the number you would like to know if the secret number is greater than: "))
    if secret > greater_int:
        return f"\nThe secret number is greater than {greater_int}"
    else:
        return f"\nThe secret number is not greater than {greater_int}"



def sum_of_digits(secret: int) -> str:
    digit_sum: int = 0
    for digit in str(secret): 
        digit_sum += int(digit)      
    return f"\nThe sum of the secret number's digits is {digit_sum}"


        
def guess_num(points: int) -> int:
    global secret_num, num_guesses, num_clues
    player_guess = int(input("\nWhat do you think the secret number is?: "))
    
    if player_guess == secret_num:
        points += 50
        print(f"\nCorrect. The secret number is {secret_num}.\nPoint Total: {points}")
        num_guesses = 0
        num_clues = 2
        secret_num = randint(1, 70)
    else:
        print(f"\nWrong. The secret number is not {player_guess}.")

    return points



if __name__ == "__main__":
    main()