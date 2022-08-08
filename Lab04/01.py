target = 72

guess = int(input("Enter your guess (0 - 100): "))

if guess < target:
    if guess < 0:
        print("Sorry, out of range, try again later.")
    elif 0 <= guess <= 100:
        print("Sorry, your guess is too low, try again later.")
elif guess > target:
    if guess > 100:
        print("Sorry, out of range, try again later.")
    elif 0 <= guess <= 100:
        print("Sorry, your guess is too high, try again later.")
elif guess == target:
    print("Congratulations, your guess is correct.")