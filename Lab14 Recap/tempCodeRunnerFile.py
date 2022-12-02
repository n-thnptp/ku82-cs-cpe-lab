msg = input()
move = int(input())
move = (move*-1) % len(msg)

output = ""
output += msg[move:] + msg[:move]

print(output)