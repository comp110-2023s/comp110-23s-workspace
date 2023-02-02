"""EX01 - Chardle - A step toward Wordle."""

__author__ = "730394864"

word: str = input("Enter a 5-character word: ")
if len(word) != 5:
    print("Error: Word must contain 5 characters")
else:
    letter: str = input("Enter a single character: ")
    if len(letter)!= 1:
        print("Error: Character must be a single character.")
    else:
        letter_correct: int = 0
        print(f"Searching for {letter} in {word}")
        if str(word[0])== str(letter):
            print(str(letter)+" found at index 0")
            letter_correct = letter_correct + 1
        if str(word[1])== str(letter):
            print(str(letter)+" found at index 1")
            letter_correct = letter_correct + 1
        if str(word[2])== str(letter):
            print(str(letter)+" found at index 2")
            letter_correct = letter_correct + 1
        if str(word[3])== str(letter):
            print(str(letter)+" found at index 3")
            letter_correct = letter_correct + 1
        if str(word[4])== str(letter):
            print(str(letter)+" found at index 4")
            letter_correct = letter_correct + 1
        if int(letter_correct) > int("1"):
            print(str(letter_correct) + f" instances of {letter} found in {word}")
        else: 
            if int(letter_correct) == int("1"):
                print(f"1 instance of {letter} found in {word}")
            else:
                print(f"No instances of {letter} found in {word}")
    