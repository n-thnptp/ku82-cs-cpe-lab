source = input().lower().replace(" ", "")
pos = input()
pos_dict = {}
decode = input()

# must have to duplicated "values" inside the dictionary
current = 0
for i in range(len(source)):
    if current == len(pos):
        break
    if source[i] not in pos_dict.values():
        pos_dict[pos[current]] = source[i]
        current += 1

output = ""
for j in decode:
    if j in list(pos_dict.keys()):
        output += pos_dict.get(j)
    else:
        output += j

print(output)