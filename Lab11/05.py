result = input()
newResult = []

for i in range(1, len(result)-1):
    newResult.append(result[i])
    
score = input()
filteredScore = []
correct = 0

for j in score:
    if j not in filteredScore:
        filteredScore.append(j)
    
for k in newResult:
    if k in filteredScore:
        correct += 1
    
if len(newResult) == 0:
    finalScore = 0
else:
    finalScore = (100 / len(newResult)) * correct

print(correct)
print("{:.2f}".format(finalScore))