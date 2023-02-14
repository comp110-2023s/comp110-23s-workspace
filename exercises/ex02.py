secret_word: str = "python"
len_guess_word= len(secret_word)
guess_word: str = input(f"What is your {len_guess_word}-letter guess?") 

while len(guess_word) != len(secret_word):
    guess_word: str = input(f"That was not {len_guess_word} letters! Try again:")
# This user has four tries to ask before it ask the user to come back
numGuess=4
i = 0
# Defining the wordle boxespython -m tools.submission exercises/ex02_one_shot_wordle.py

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Establishing a variable to store the emoji of the persons guess
variable_index: int = 0
guess_emoji: str = ""
# creating our loop to establish if the index is less than the length of our word (python)
while variable_index < len(secret_word):
     if guess_word[variable_index] == secret_word[variable_index]:
        guess_emoji = f"{guess_emoji}{GREEN_BOX}" 
     else:
        letter_exists: bool = False
        alt_index= int = 0
        while not letter_exists and alt_index < len(secret_word):
         if guess_word[index] == secret_word[alt_index]:
            letter_exists: bool = True
            result_emoji = f"{result_emoji}{YELLOW_BOX}"
         else:
               alt_index = alt_index + 1

if not letter_exists:
         result_emoji = f"{result_emoji}{WHITE_BOX}"
         
         index = index + 1 
print(result_emoji)
   
   
if guess_word == secret_word:
      print("Woo! You got it!")
elif len (guess_word) == len(secret_word):
      print("Not quite. Play again soon! ")