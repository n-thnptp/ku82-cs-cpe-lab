name_1 = input()
name_2 = input()

switch = False
result = ""

n1_found = []
for v_1 in range(len(name_1)):
    if name_1[v_1] in 'aeiou':
        n1_found.append(v_1)

if len(n1_found) <= 1:
    result += name_1
else:
    result += name_1[:n1_found[1]]

n2_found = []
for v_2 in range(len(name_2)):
    if name_2[v_2] in 'aeiou':
        n2_found.append(v_2)
    
if len(n2_found) < 1:
    result += name_2
else:
    result += name_2[n2_found[0]+1:]

print(result)