msg = input()
replace = "-_=.$"

output = ""
index = 0
for i in msg:
    if i not in replace:
        if index == 0:
            output += i.lower()
        else:
            if msg[index-1] in replace:
                output += i.upper()
            else:
                output += i
    index += 1
output2 = output[0].lower() + output[1:]
print(output2)