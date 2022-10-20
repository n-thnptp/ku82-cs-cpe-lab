# h a n g m a n
# - - - - - - -
# 0 1 2 3 4 5 6

word = input()
chara = ""
ans = ["-"]*len(word)
while True:
    guess = input()
    
    if guess == "0":
        break
    else:
        chara += guess
    
for i in range(len(word)):
    if word[i] in chara:
        ans[i] = word[i]
        
print("".join(ans))