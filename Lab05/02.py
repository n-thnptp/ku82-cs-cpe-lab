import math

hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
buyAmt = int(input("Enter shopping amount: "))

total_h = math.ceil(hours + (minutes / 60))

if (hours > 20) or (minutes > 59) or ((minutes > 0) and (hours == 20)) or (hours < 0) or (minutes < 0):
    print("Invalid time.")

else:
    if (total_h <= 2) or (buyAmt > 3000): # if buy amount is more than 3000 / total hours lower than or equal to 2
        print("No charge, thank you.")

    elif (buyAmt > 300) and (buyAmt < 3000): # if buy amount is between 300 - 3000
        if total_h <= 4: # "เมื่อลูกค้าซื้อสินค้าตั้งแต่ 300 – 3,000 บาท ให้จอดฟรีเพิ่มในชั่วโมงที่ 3 และ 4"
            print("No charge, thank you.")
        else:
            cost = (total_h - 4) * 50
            print("Total amount due is {} Baht, thank you.".format(cost))

    else:
        if total_h < 5:
            cost = (total_h - 2) * 20
            print("Total amount due is {} Baht, thank you.".format(cost))

        else: # if total hours is over 5 hours
            cost = 40 + ((total_h - 4) * 50)
            print("Total amount due is {} Baht, thank you.".format(cost))