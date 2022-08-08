import math

hours = int(input("Enter number of hours: "))
mins = int(input("Enter number of minutes: "))

if (hours < 0 or mins < 0):
    print("Input Error!")
else:    
    t_mins = (hours * 60) + mins
    cost = 0
    if t_mins <= 15:
        print("No charge, thanks")
    elif t_mins <= 120:
        print("Total amount due is 10 Bahts.")
    elif t_mins > 120:
        no_h = math.ceil((t_mins - 120) / 60)
        cost = 10 + (no_h * 10)
        print(f"Total amount due is {cost} Bahts.")