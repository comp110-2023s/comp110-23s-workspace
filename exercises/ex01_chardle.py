"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730558596"

user_input: str = input("Enter a 5-character word: ")
if len(user_input) != 5:
    print("Error: Word must contain 5 characters ")
    exit()

char_val = input("Enter a single character: ")
print("Searching for " + char_val + " in " + user_input) 
if len(char_val) != 1:
    print("Error: Character must be a single character. ")
    exit()

match_count = 0

if char_val[0] == user_input:
    print(char_val + " found at index 0 ")
    match_count += 1
if char_val[1] == user_input:
    print(char_val + " found at index 1 ")
    match_count += 1
if char_val[2] == user_input:
    print(char_val + " found at index 2 ")
    match_count += 1
if char_val[3] == user_input:
    print(char_val + " found at index 3 ")
    match_count += 1
if char_val[4] == user_input:
    print(char_val + " found at index 4 ")
    match_count += 1 

if match_count > 1:
    print(str(match_count) + " instances of " + char_val + " found in " + user_input)
elif match_count == 1:
     print(str(match_count) + " instance of " + char_val + " found in " + user_input)
else:
    print(" No instnaces of " + char_val + " found in " + user_input)