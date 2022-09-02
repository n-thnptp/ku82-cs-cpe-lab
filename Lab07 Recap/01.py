x = float(input())

if x % 1 == 0:
    print("{:.0f} is an integer.".format(x))
else:
    print("{} is not an integer.".format(x))