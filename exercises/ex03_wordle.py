"""EX03 - Structured Wordle!"""

__author__ = "730558596"

def contains_char(user_word: str, correct_letter: str) -> bool:
    """"Given the string the users word, the user_word will be searched for the correct the letter."""
    assert len(correct_letter) == 1
    # int_idx = 0

    # while int_idx < len(user_word):
    #     if correct_letter == user_word[int_idx]:
    #         return True
    #     else:
    #         return False
    #     int_idx = int_idx + 1 
    if correct_letter in user_word: 
        return True
    else:
        return False

def emojified(guess_word: str, secret_word: str) -> str:
    """Given the guessword, check to see if it is matching with the correct word. Print the result of the match with the emoji."""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    indx = 0
    result_emoji: str = ""

    while indx < len(secret_word):
        if guess_word[indx] == secret_word[indx]:
            result_emoji = f"{result_emoji}{GREEN_BOX}"
        else:
            if contains_char(secret_word,guess_word[indx]) == True: 
                result_emoji= f"{result_emoji}{YELLOW_BOX}"
                exit
            if contains_char(secret_word,guess_word[indx]) == False:
                result_emoji=f"{result_emoji}{WHITE_BOX}"
        indx = indx + 1


    return( result_emoji)

def input_guess(expected_length: int) -> str:
    """If the word is not the expected length, ask the user to try again."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        if len(user_guess) < expected_length or len(user_guess) > expected_length:
            user_guess= input(f"That wasn't {expected_length} chars! Try again: ")
    return user_guess

def main () -> None:
    """ This is the entrypoint of the program and the main game loop."""
    ind: int = 1 
    scr_word: str = "codes"
    user_guess: str = ""
    while user_guess != scr_word:
        print(f"== Turn {ind}/6 ==")
        user_guess = input_guess(len(scr_word))
        print(emojified(user_guess, scr_word))
        if ind <= 6 and user_guess != scr_word:
            ind = ind + 1
        if ind >= 1 and user_guess == scr_word:
            print (f"You won in {ind}/6 turns!")
            user_guess = scr_word
        if ind == 7:
            print("X/6 - Sorry, try again tomorrow!")
            user_guess = scr_word
        

if __name__ == "__main__":
    main()
