"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730558596"

user_input: str = input("Enter a 5-character word: ")
if len(user_input) != 5:
    print(" Error: Word must contain 5 characters.")
    quit()
char_val = input("Enter a single character: ")
print(" Searching for " + char_val + " in " + user_input) 
if len(char_val) != 1:
    print("Error: Character must be a single character. ")
    quit()
count = 0

if user_input[0] == char_val:
    print(char_val + " found at index 0 ")
    count += 1 
if user_input[1] == char_val:
    print(char_val + " found at index 1 ")
    count += 1
if user_input[2] == char_val:
    print(char_val + " found at index 2 ")
    count += 1
if user_input[3] == char_val:
    print(char_val + " found at index 3 ")
    count += 1
if user_input[4] == char_val:
    print(char_val + " found at index 4 ")
    count += 1 
print(str(count) + " instance of " + char_val + " found in " + user_input)