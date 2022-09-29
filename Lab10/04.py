def find_mode(l):
    count = [0]*11
    for j in l:
        count[j] += 1
    for i in range(len(count)):
        if count[i] == max(count):
            print(i)
    
    
num_list = []

i = 0
while i < 20:
    n = int(input("Enter score: "))
    if n < 0 or n > 10:
        print("Score is out of range.")
    else:
        num_list.append(n)
        i += 1    
        
print("-----")
print("Original list:")
print(num_list)
print("Mode of scores:")
find_mode(num_list)