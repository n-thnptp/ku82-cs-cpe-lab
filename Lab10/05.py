num_list = []
while True:
    n = int(input())
    if n == -1:
        break
    else:
        num_list.append(n)
        
new_list = [num_list[0]]
for i in range(1, len(num_list)):
    if i == 0 or i == i-1:
        pass
    else:
        curr = num_list[i]
      
        if curr >= new_list[-1]:
            new_list.append(curr)
        else:
            continue
      
    
print(new_list)