def check_order(l):
    if len(l) == 0:
        print("The list is empty.")
    elif l == sorted(l):
        print("The list is in non-decreasing order.")
    elif l == sorted(l, reverse=True):
        print("The list is in non-increasing order.")

num = []
while True:
    n = int(input("Enter a number (-1 to end): "))
    
    if n == -1:
        break
    else:
        num.append(n)
        
print("-----")
print("Original list:")
print(num)
check_order(num)