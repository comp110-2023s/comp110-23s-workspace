"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730556365"

five_letter_word: str = input("Enter a 5-character word: ")
if (len(five_letter_word) != 5):
    print("Error: Word must contain five characters")
    exit()

one_letter: str = input("Enter a single character: ")
if (len(one_letter) != 1):
    print("Error: Character must be a single character")
    exit()

print("Searching for " + one_letter + " in " + five_letter_word)

letter_count: int = 0
if (five_letter_word[0] == one_letter):
    print(one_letter + " found at index 0")
    letter_count = letter_count + 1
if (five_letter_word[1] == one_letter):
    print(one_letter + " found at index 1")
    letter_count = letter_count + 1
if (five_letter_word[2] == one_letter):
    print(one_letter + " found at index 2")
    letter_count = letter_count + 1
if (five_letter_word[3] == one_letter):
    print(one_letter + " found at index 3")
    letter_count = letter_count + 1
if (five_letter_word[4] == one_letter):
    print(one_letter + " found at index 4")
    letter_count = letter_count + 1

if (letter_count > 1):
    print(str(letter_count) + " instances of " + one_letter + " found in " + five_letter_word)
elif (letter_count == 1):
    print(str(letter_count) + " instance of " + one_letter + " found in " + five_letter_word)
else:
    print("No instances of " + one_letter + " found in " + five_letter_word)