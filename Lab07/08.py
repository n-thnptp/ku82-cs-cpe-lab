n = int(input())
x = 0
a = 1
count = 0
while a < n:
    b = 1
    while a >= b:
        if ((a**2 + b**2) == n**2):
            if (a+b == x):
                pass
            else:
                count += 1
            x = a+b
        b += 1
    a += 1
print(count)
