message = input()
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
count = 0
for i in message:
    if i in vowels:
        count += 1

print(count)