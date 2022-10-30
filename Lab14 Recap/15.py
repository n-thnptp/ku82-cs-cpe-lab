msg = input()
msg = msg.split(" ")
result = ""
ls = []

for i in range(len(msg)):
    if msg[i] not in ['for', 'and', 'with', 'of']:
        for j in range(len(msg[i])):
            if msg[i][j].islower() and j == 0:
                result += msg[i][j].upper()
            elif msg[i][j].isupper() and j == 0:
                result += msg[i][j].upper()
            else:
                result += msg[i][j].lower()
        ls.append(result)
        result = ""
    else:
        ls.append(msg[i])
        
print(" ".join(ls))