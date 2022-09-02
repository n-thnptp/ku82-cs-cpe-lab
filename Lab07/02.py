n = int(input("Enter a number: "))

i = n
if n <= 0 or n > 26:
    print("Invalid input, program terminates.")
else:
    while 0 <= i <= 26:
        j = 0
        while j < i:
            print(chr(ord("A") + j), end="")
            j += 1
        print()
        i -= 1
