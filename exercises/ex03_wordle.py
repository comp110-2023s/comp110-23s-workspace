"""EX03 - structured wordle!"""

__author__ = "730575328"

def contains_char(word: str, char: str) -> bool:
  """Searches the indexes of the given word for the given character"""
  assert len(char) == 1
  idx: int = 0 
  while idx < len(word):
    if char == word[idx]:
      return True
    idx = idx + 1
  return False

def emojified (guess: str, secret: str) -> str:
  """Returns a string of coded emojis for each letter of the guess"""
  assert len(guess) == len(secret)

  WHITE_BOX: str = "\U00002B1C"
  GREEN_BOX: str = "\U0001F7E9"
  YELLOW_BOX: str = "\U0001F7E8"
  emoji_string: str = ""

  idx: int = 0 
  while idx < len(guess):
    result = contains_char(secret, guess[idx])
    if result == True:
        if secret[idx] == guess[idx]:
          emoji_string += GREEN_BOX
        else:
          emoji_string += YELLOW_BOX
    else:
        emoji_string += WHITE_BOX
    idx = idx + 1
 
  return emoji_string

def input_guess(length: int) -> str:
  """Prompts user for a guess that is within the right number of characters"""
  guess: str = input("Enter a " + str(length) + " character word:")
  while len(guess) != length:
    guess = input("That wasn't " + str(length) + " chars! Try again:")
  return guess

def main() -> None:
  """The entrypoint of the program and main game loop"""
  
  secret: str = "codes"
  turn_idx: int = 1

  while turn_idx <= 6:
    print("=== Turn " + str(turn_idx) + "/6 ===")
    guess = input_guess(len(secret))
    print(emojified(guess,secret))
    if guess == secret:
      print("You won in " + str(turn_idx) + "/6 turns!" )
      return
    turn_idx = turn_idx + 1
print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
  main()