import math

mins = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")

# mins to days
mins_to_days = mins / 1440

if (float(mins_to_days) % 1) >= 0.5:
    days = math.ceil(mins_to_days)
else:
    days = round(mins_to_days)

print(">>> {} days before due.".format(days))

if days < 2:
    print(">>> I will do the assignment.")

elif days > 5:
    print(">>> I will not do the assignment.")

elif temp > 40 or (temp > 25 and (rain == "y" or rain == "Y")):
    print(">>> I will not do the assignment.")

else:
    print(">>> I will do the assignment.")