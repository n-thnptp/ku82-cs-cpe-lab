data = []
while True:
    msg = input()
    if msg == "":
        break
    else:
        data.append(msg)
        max_length = 0
        for word in data:
            if len(word) > max_length:
                max_length = len(word)
                result = word

print(result)