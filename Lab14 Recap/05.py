word = input().lower()

count = ""
for i in range(len(word)):
    if i+1 < len(word):
        if word[i] < word[i+1]:
            count = word[:i+2]
        else:
            break
        
if count == "" and word != "":
    count = word[0]
    print(len(count))
else:        
    print(len(count))