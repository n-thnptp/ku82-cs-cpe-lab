costs = float(input("Enter buying amount: "))

if (costs < 1000):
    print("Amount due after discount is %.2f baht." %costs)
elif (costs >= 1000 and costs < 3000):
    disc = costs * 0.90
    print("Amount due after discount is %.2f baht." %disc)
elif (costs >= 3000):
    disc = costs * 0.85
    print("Amount due after discount is %.2f baht." %disc)
else:
    print("Error")