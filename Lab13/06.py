# non-increasing / non-decreasing every iteration == the same
# steps to check the num list
# 1. empty 2. non-increasing / non-decreasing 3. non-decreasing 4. non-indecreasing 5. random

def check_order(l):
    if len(l) == 0:
        print("The list is empty.")
    else:
        check = l.count(l[0])
        if check == len(l):
            print("The list is in non-increasing and non-decreasing order.")
        elif l == sorted(l):
            print("The list is in non-decreasing order.")
        elif l == sorted(l, reverse=True):
            print("The list is in non-increasing order.")
        else:
            random = False
            for i in range(1, len(l)):
                if i+1 < len(l):
                    prev, current, next_n = l[i-1], l[i], l[i+1]
                    if prev <= current <= next_n or prev >= current >= next_n:
                        random = False
                    else:
                        random = True
            if random == True:
                print("The list is in random order.")

num = []
while True:
    n = int(input("Enter a number (-1 to end): "))
    
    if n > 100 or n < 0:
        if n == -1:
            break
        else:
            print("Number is out of range.")
    else:
        num.append(n)
        
print("-----")
print("Original list:")
print(num)
check_order(num)