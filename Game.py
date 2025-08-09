import random
n = random.randint(1,10)
guess = -1
n_guess = 0
while n != guess :
    try :
        guess = int(input("Guess the number: "))
        n_guess = n_guess + 1
        if n > guess :
            print("Guess the higher number")
        elif n < guess :
            print("Guess the lower number")
        else :
            print("You won the game and your attempt is", n_guess , "and the number is", n)
    except :
        print("Please enter a valid number")
    