"""EX03 - Structured Wordle."""

__author__ = "730556365"


def contains_char(secret_word: str, search_char: str) -> bool:
    """Checks if a word contains a certain character."""
    assert len(search_char) == 1   # checks that only one letter is inputed for the 'search_char' parameter
    char_in_word: bool = False
    idx: int = 0
    while (char_in_word is False) and (idx < len(secret_word)):
        if (search_char == secret_word[idx]):
            char_in_word = True
        else: # move to the next letter
            idx = idx + 1
    return char_in_word


def emojified(player_guess: str, secret_word: str) -> str:
    """Returns emojis indicating the accuracy of the guessed word."""
    assert len(player_guess) == len(secret_word) # causes an error message if an inputed guess has the incorrect number of letters
    WHITE_BOX: str = "\U00002B1C" # means the guessed letter is not in the secret word at all
    GREEN_BOX: str = "\U0001F7E9" # means the guessed letter is in the secret word and in the right spot
    YELLOW_BOX: str = "\U0001F7E8" # means the guessed letter is in the secret word but in a different spot
    guess_score: str = ""
    idx: int = 0
    while (idx < len(secret_word)): # loop that checks both if each letter of the guess is in the secret word and if it's in the correct spot
        if (player_guess[idx] == secret_word[idx]):
            guess_score = f"{guess_score}{GREEN_BOX}"
        else:
            yellow_or_white: bool = contains_char(secret_word, player_guess[idx])
            if (yellow_or_white is True):
                guess_score = f"{guess_score}{YELLOW_BOX}"
            else: # if 'yellow_or_white' is False
                guess_score = f"{guess_score}{WHITE_BOX}"
        idx = idx + 1   # move to the next letter
    return guess_score

def input_guess(expected_guess_len: int) -> str:
    """Stores and returns the guess inputed by a player."""
    player_guess: str = input(f"Enter a {expected_guess_len} character word: ")
    while (len(player_guess) != expected_guess_len): # prints an error message if an inputed guess has the incorrect number of letters
        player_guess = input(f"That was not {expected_guess_len} letters! Try again: ")
    return player_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    attempt_num: int = 1
    playing: bool = True
    while (playing is True) and (attempt_num <= 6): # loop that gives the player six chances to guess the correct word
        print(f"=== Turn {attempt_num}/6 ===")
        player_guess = input_guess(len(secret_word))
        guess_score = emojified(player_guess, secret_word)
        print(guess_score)
        if (player_guess == secret_word):
            print(f"You won in {attempt_num}/6 turns!")
            playing = False   # exits the game if the secret word is correctly guessed
        else: 
            attempt_num = attempt_num + 1
    if (playing is True):
        print("X/6 - Sorry, try again tomorrow!")

if (__name__ == "__main__"): # allows us to run the program as a module
    main()