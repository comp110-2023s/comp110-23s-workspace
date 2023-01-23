"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730575328"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

letter: str = input("Enter a single character: ")

if len(letter) != 1:
    print("Error: Character must be a single character.")
    exit()

x: int = 0
print("Searching for " + letter + " in " + word)

if (word[0]) == letter:
    print(word[0] + " found at index 0")
if (word[1]) == letter:
    print(word[1] + " found at index 1")
if (word[2]) == letter:
    print(word[2] + " found at index 2")
if (word[3]) == letter:
    print(word[3] + " found at index 3")   
if (word[4]) == letter:
    print(word[4] + " found at index 4") 

if (word[0]) == letter:
    x = x + 1
if (word[1]) == letter:
    x = x + 1
if (word[2]) == letter:
    x = x + 1
if (word[3]) == letter:
    x = x + 1
if (word[4]) == letter:
    x = x + 1
if x == 0:
    print("No")

if x != 1:
    print(x,"instances of", letter, "found in", word)
else:
    print(x,"instance of", letter, "found in", word)