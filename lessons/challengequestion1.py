""" Example Enviormental digram for conditonals """
secret: int = 3
guess: int = 4

if guess == secret:
    print ("sucess!")
    print (str(guess) + " is the secret number!")
else:
    guess = guess + 1 
    if guess == secret:
        print("Sucess on 2nd try!")
    else: 
        print("Wrong guess.:(")
        if (guess == secret -1):
            print("Hint: The guess of " + str(guess) + "is off by only one number!")