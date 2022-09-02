target = int(input("Enter a target (4-digit integer): "))
guess = int(input("Enter your guess (4-digit integer): "))

while True:
    if target == guess:
        print("Congratulations, you just mastered my mind! !")
    