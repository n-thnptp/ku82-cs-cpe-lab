a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

while True:
    total = a % b # 20 % 8 = 4

    while total != 0:
        c = b # a = 8
        d = total # b = 4
        e = c % d # c = 0
        
        if e == 0:
            print("  >> gcd({}, {}) = {}".format(a, b, total))
            break
        
    break
    