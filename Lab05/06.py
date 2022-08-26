nums = int(input())

sum = 0

while nums != 0:
    sum += (nums % 10)
    nums = nums // 10

if sum % 9 != 0:
    sum = sum % 9
    print("No {:.0f}".format(sum))
else:
    print("Yes {}".format(sum))