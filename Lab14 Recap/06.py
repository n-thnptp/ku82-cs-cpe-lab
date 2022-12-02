msg = input()
move = int(input())
move = move % len(msg)

output = ""
if move >= 0:
    output += msg[-move:] + msg[:-move]
else:
    output += msg[abs(move):] + msg[:abs(move)]

print(output)