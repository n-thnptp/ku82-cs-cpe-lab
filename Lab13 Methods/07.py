# slice between first string and last string before number
text = "AB12XY23"
ext = []

j = 0
for i in range(len(text)):
    test = text[i]
    if text[i].isdigit():
        ext.append(text[j:i])
        j = i
        
print(ext)