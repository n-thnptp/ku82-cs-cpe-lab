yr = int(input("Enter year: "))

if yr <= 0:
    print("Invalid year.")
else:

    if yr % 4 == 0 and not yr % 100 == 0:
        print("{} is a leap year.".format(yr))
    elif yr % 400 == 0:
        print("{} is a leap year.".format(yr))
    else:
        print("{} is not a leap year.".format(yr))