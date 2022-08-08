target = 72

num = int(input("Enter your guess (0 - 100): "))

if 0 <= num <= 100:
    if num == target:
        print("Congratulations, your guess is correct.")
    elif num != target:
        print("Sorry, your guess is wrong, try again later.")
else:
    print("Sorry, out of range, try again later.")
