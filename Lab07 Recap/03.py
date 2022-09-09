# 1 = sun , 2 = mon , 3 = tues , ... , 7 = sat

# คุณเตรียมรูปที่มีชื่อไฟล์ว่า good-morning-monday.png สำหรับเช้าวันจันทร์ ในช่วง 04.01 - 12.00 น.

# รูปที่มีชื่อไฟล์ว่า good-afternoon-monday.png สำหรับบ่ายวันจันทร์ ในช่วง 12.01 - 18.00 น.

# รูปที่มีชื่อไฟล์ว่า good-evening-monday.png สำหรับเย็นวันจันทร์ ในช่วง 18.01 - 22.00 น.

# และรูปที่มีชื่อไฟล์ว่า good-night-monday.png สำหรับบอกลาวันจันทร์ ในช่วง 22.01 - 04.00 น.

day = int(input())
hours = int(input())
mins = int(input())

if day == 1:
    if ((4 <= hours <= 11 and 1 <= mins <= 59) or (hours == 12 and mins == 0)):
        print("good-morning-sunday.png")
    elif ((12 <= hours <= 17 and 1 <= mins <= 59) or (hours == 18 and mins == 0)):
        print("good-afternoon-sunday.png")
    elif ((18 <= hours <= 21 and 1 <= mins <= 59) or (hours == 22 and mins == 0)):
        print("good-evening-sunday.png")
    elif ((22 <= hours <= 23 and 1 <= mins <= 59) or (0 <= hours <= 4 and 0 <= mins <= 59)):
        print("good-night-sunday.png")

elif day == 2:
    if ((4 <= hours <= 11 and 1 <= mins <= 59) or (hours == 12 and mins == 0)):
        print("good-morning-monday.png")
    elif ((12 <= hours <= 17 and 1 <= mins <= 59) or (hours == 18 and mins == 0)):
        print("good-afternoon-monday.png")
    elif ((18 <= hours <= 21 and 1 <= mins <= 59) or (hours == 22 and mins == 0)):
        print("good-evening-monday.png")
    elif ((22 <= hours <= 23 and 1 <= mins <= 59) or (0 <= hours <= 4 and 0 <= mins <= 59)):
        print("good-night-monday.png")

elif day == 3:
    if ((4 <= hours <= 11 and 1 <= mins <= 59) or (hours == 12 and mins == 0)):
        print("good-morning-tuesday.png")
    elif ((12 <= hours <= 17 and 1 <= mins <= 59) or (hours == 18 and mins == 0)):
        print("good-afternoon-tuesday.png")
    elif ((18 <= hours <= 21 and 1 <= mins <= 59) or (hours == 22 and mins == 0)):
        print("good-evening-tuesday.png")
    elif ((22 <= hours <= 23 and 1 <= mins <= 59) or (0 <= hours <= 4 and 0 <= mins <= 59)):
        print("good-night-tuesday.png")

elif day == 4:
    if ((4 <= hours <= 11 and 1 <= mins <= 59) or (hours == 12 and mins == 0)):   
        print("good-morning-wednesday.png")
    elif ((12 <= hours <= 17 and 1 <= mins <= 59) or (hours == 18 and mins == 0)):
        print("good-afternoon-wednesday.png")
    elif ((18 <= hours <= 21 and 1 <= mins <= 59) or (hours == 22 and mins == 0)): 
        print("good-evening-wednesday.png")
    elif ((22 <= hours <= 23 and 1 <= mins <= 59) or (0 <= hours <= 4 and 0 <= mins <= 59)):
        print("good-night-wednesday.png")

elif day == 5:
    if ((4 <= hours <= 11 and 1 <= mins <= 59) or (hours == 12 and mins == 0)):
        print("good-morning-thursday.png")
    elif ((12 <= hours <= 17 and 1 <= mins <= 59) or (hours == 18 and mins == 0)):
        print("good-afternoon-thursday.png")
    elif ((18 <= hours <= 21 and 1 <= mins <= 59) or (hours == 22 and mins == 0)):
        print("good-evening-thursday.png")
    elif ((22 <= hours <= 23 and 1 <= mins <= 59) or (0 <= hours <= 4 and 0 <= mins <= 59)):
        print("good-night-thursday.png")

elif day == 6:
    if ((4 <= hours <= 11 and 1 <= mins <= 59) or (hours == 12 and mins == 0)):
        print("good-morning-friday.png")
    elif ((12 <= hours <= 17 and 1 <= mins <= 59) or (hours == 18 and mins == 0)):
        print("good-afternoon-friday.png")
    elif ((18 <= hours <= 21 and 1 <= mins <= 59) or (hours == 22 and mins == 0)):
        print("good-evening-friday.png")
    elif ((22 <= hours <= 23 and 1 <= mins <= 59) or (0 <= hours <= 4 and 0 <= mins <= 59)):
        print("good-night-friday.png")

elif day == 7:
    if ((4 <= hours <= 11 and 1 <= mins <= 59) or (hours == 12 and mins == 0)):
        print("good-morning-saturday.png")
    elif ((12 <= hours <= 17 and 1 <= mins <= 59) or (hours == 18 and mins == 0)):
        print("good-afternoon-saturday.png")
    elif ((18 <= hours <= 21 and 1 <= mins <= 59) or (hours == 22 and mins == 0)):
        print("good-evening-saturday.png")
    elif ((22 <= hours <= 23 and 1 <= mins <= 59) or (0 <= hours <= 4 and 0 <= mins <= 59)):
        print("good-night-saturday.png")
