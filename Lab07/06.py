#Enter height: 5
#Enter width: 6
#* * * * * *    i = 0
 #* * * * * *   i = 1
#* * * * * *    i = 2
 #* * * * * *   i = 3
#* * * * * *    i = 4


height = int(input("Enter height: "))
width = int(input("Enter width: "))

if height <= 0 or width <= 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    while i < height:
        j = 0
        while j < width:
            if i % 2 == 0:
                print("* ", end="")
            else:
                print(" *", end="")
            j += 1
        print()
        i += 1
        