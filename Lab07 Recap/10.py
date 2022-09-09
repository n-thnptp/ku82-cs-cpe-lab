num = int(input())

i = 0
output = 0
while num > 0:
    i = num % 10
    if i % 2 != 0:
        output += i
    num //= 10
    i = 0

if output <= 0:
    print("-1")
else:
    print(output)