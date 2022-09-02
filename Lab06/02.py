target = 72

i = 1
while 0 <= i <= 100:
    guess = int(input("Enter your guess: "))

    if guess > 72 and guess <= 100:
        print("Sorry, your guess is too high.")
        i += 1
    
    elif guess < 72 and guess >= 0:
        print("Sorry, your guess is too low.")
        i += 1
    
    elif guess == 72:
        print("Congratulations, your guess is correct.")
        print("Total number of guesses is {}.".format(i))
        break

    elif guess < 0 or guess > 100:
        print("Sorry, your guess is out of range.")
        i += 1