# Enter a number: 5
# 0! = 1 = 1
# 1! = 1 = 1
# 2! = 2 x 1 = 2
# 3! = 3 x 2 x 1 = 6
# 4! = 4 x 3 x 2 x 1 = 24
# 5! = 5 x 4 x 3 x 2 x 1 = 120


n = int(input("Enter a number: "))

if n < 0:
    print("Invalid input, program terminates.")
elif n == 0:
    print("0! = 1 = 1")
else:
    print("0! = 1 = 1")
    i = 1
    fac = 1
    indent = "1"
    while i <= n:
        print("{}! = {} = {}".format(i, indent, fac))
        i += 1
        fac *= i
        indent = str(i) + " x " + indent