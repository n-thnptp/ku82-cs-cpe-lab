num = int(input())

i = 0
output = 1
count = 0
j = 0
while num > 0:
    i = num % 10
    if i % 2 == 0:
        output *= i
    else:
        count += 1
    num //= 10
    i = 0
    j += 1

if j == count:
    print("-1")
else:
    print(output)