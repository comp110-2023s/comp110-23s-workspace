"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730466092"

five_cha_word: str=input("Enter a 5-character word: ")
if(len(five_cha_word)!=5):
    print("Word must contain 5 characters")
    exit()
else:
    single_cha: str=input("Enter a single character: ")
if(len(single_cha)!=1):
    print("Character must be a single character")
    exit()
else:
    print(f"Searching for {single_cha} in {five_cha_word}...")

char_amount: int=0

if(single_cha==five_cha_word[0]):
    char_amount += 1
    print(single_cha + " found at index 0")
if(single_cha==five_cha_word[1]):
    char_amount += 1
    print(single_cha + " found at index 1")
if(single_cha==five_cha_word[2]):
    char_amount += 1
    print(single_cha + " found at index 2")
if(single_cha==five_cha_word[3]):
    char_amount += 1
    print(single_cha + " found at index 3")
if(single_cha==five_cha_word[4]):
    char_amount += 1
    print(single_cha + " found at index 4")
if(char_amount == 0):
    print(f"No instances of {single_cha} found in {five_cha_word}")
else:
    print(f"{char_amount} instances of {single_cha} found in {five_cha_word}")