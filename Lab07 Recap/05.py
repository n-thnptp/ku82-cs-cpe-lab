num = int(input("Enter a number: "))
digit = int(input("Enter a digit: "))

if num < 0:
    print("Invalid number.")
    if digit > 9:
        print("Invalid digit.")
elif digit > 9:
    print("Invalid digit.")
    if num < 0:
        print("Invalid number.")
else:
    i = 0
    count = 0
    while num > 0:
        i = num % 10
        num = num // 10
        if i % digit == 0:
            count += 1
    if count == 1:
        print("Digit {} occurs {} time.".format(digit, count))
    else:
        print("Digit {} occurs {} times.".format(digit, count))