# copompuputeper papapripikapa
# c o [p o] m p u [p u ] t e  [p  e ] r
# 0 1  2 3  4 5 6  7 8   9 10  11 12 13
# computer
# if current alphabet (i) is "p" and the next one is the same as a vowel before i then don't append these (skip both)
# abcdefghijk
# 012345678910
def getResult(x):
    strOut = ""
    for dc in x:
        strOut += dc
    print(strOut)

word = input()
vowels = ["a", "e", "i", "o", "u"]
wordList = []

i = 0
while i < len(word):
    wordList.append(word[i])
    current = word[i]
    sliced = word[i:i+2]
    if word[i] in vowels and word[i:i+3] == word[i] + "p" + word[i]:
        i += 2
    i += 1
        
getResult(wordList)