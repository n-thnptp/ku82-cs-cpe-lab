n2_found = []
for v_2 in range(len(name_2)):
    if name_2[v_2] in 'aeiou':
        n2_found.append(v_2)
    
result += name_2[n2_found[0]+1:]

print(result)