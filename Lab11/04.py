word = input()

guess_list = []
correct = 0
while True:
    guess = input()
    if guess == "0":
        break
    else:
        guess_list.append(guess)

for j in word:
    if j in guess_list:
        correct += 1
        
print("{:d}/{:d}".format(correct, len(word)))