message = input()
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
output = ""
for i in message:
    if i in vowels:
        continue
    else:
        output += i
print(output)