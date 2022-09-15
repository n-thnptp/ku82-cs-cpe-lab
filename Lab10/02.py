num_list = []
while True:
    n = int(input("Enter a number (0 to end): "))
    if n == 0:
        break
    elif n < 1 or n > 999:
        print("Number is out of range.")
    else:
        num_list.append(n)
        
print("Original list:")
print(num_list)

print("Accumulative Sum:")
result = 0
for i in range(len(num_list)):
    num = num_list[i]
    result += num
    print(result)