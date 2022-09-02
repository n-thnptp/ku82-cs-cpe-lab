n = int(input("Enter a number: "))
i = 0

if n <= 0 or n > 26:
    print("Invalid input, program terminates.")
else:
    while i < n:
        j = 0
        while j <= i:
            print(chr(ord("A") + j), end="")
            j += 1
        print()
        i += 1
    