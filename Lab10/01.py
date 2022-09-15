num_list = []
i = 0
while i < 20:
    score = int(input("Enter score: "))
    if score < 0 or score > 10:
        print("Score is out of range.")
    else:
        num_list.append(score)
        i += 1
    
print("Original list:")
print(num_list)

n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
for j in range(len(num_list)):
    if num_list[j] == 0:
        n0 += 1
    elif num_list[j] == 1:
        n1 += 1
    elif num_list[j] == 2:
        n2 += 1
    elif num_list[j] == 3:
        n3 += 1
    elif num_list[j] == 4:
        n4 += 1
    elif num_list[j] == 5:
        n5 += 1
    elif num_list[j] == 6:
        n6 += 1
    elif num_list[j] == 7:
        n7 += 1
    elif num_list[j] == 8:
        n8 += 1
    elif num_list[j] == 9:
        n9 += 1
    elif num_list[j] == 10:
        n10 += 1
        
print(" 0", "*"*n0)
print(" 1", "*"*n1)
print(" 2", "*"*n2)
print(" 3", "*"*n3)
print(" 4", "*"*n4)
print(" 5", "*"*n5)
print(" 6", "*"*n6)
print(" 7", "*"*n7)
print(" 8", "*"*n8)
print(" 9", "*"*n9)
print("10", "*"*n10)