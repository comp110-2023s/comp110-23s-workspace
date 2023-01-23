"""EX01 - Chardle - A cute step toward Wordle."""

_author_ = "730308175"

word = str(input('Enter a 5-character word:' )) #need to establish word
if (len(word) != 5): 
    print('Error: Word must contain 5 characters')
    exit() #exit program if word does not meet requirements

letter = str(input('Enter a single character:' )) #need to establish character
if (len(letter) != 1):
    print('Error: Character must be a single character.')
    exit() #exit program if more than one character are assessed

print(f'Searching for {letter} in {word}') #need to show that the program is searching for letter in word

letter_count = 0 #start count for letter in word from zero
if (letter == word[0]): #find if the letter is in the word at index 0
    letter_count += 1 #count if there is letter at index 0
    print(f'{letter} found at index 0')
if (letter == word[1]): #find if the letter is in the word at index 1
    letter_count += 1 #add to previously updated letter_count
    print(f'{letter} found at index 1')
if (letter == word[2]): #find if the letter is in the word at index 2
    letter_count += 1 #add to previously updated letter_count
    print(f'{letter} found at index 2')
if (letter == word[3]): #find if the letter is in the word at index 3
    letter_count += 1 #add to previously updated letter_count
    print(f'{letter} found at index 3')
if (letter == word[4]): #find if the letter is in the word at index 4
    letter_count += 1 #add to previously updated letter_count
    print(f'{letter} found at index 4')  
if letter_count > 0: #add to previously updated letter_count
    print(f'{letter_count} instances of {letter} found in {word}')
else:
    print(f'No instances of {letter} found in {word}') #show total number of letter instances in the word