i = 0
while True:
    nums = int(input("Enter number: "))

    check_odd = nums % 2
    if nums >= 0:

        if check_odd != 0:
            i += 1
        else:
            pass
    else:
        break
    
print("Received {} odd numbers".format(i))