max_score = int(input())
requirement = float(input())
n = int(input())

scores = []
i = 0
while i < n:
    scores_in = int(input())
    scores.append(scores_in)
    i += 1
    
percent = []
for p in scores:
    num = (p / max_score) * 100
    percent.append(num)
    
count = 0
for n in percent:
    if n < requirement:
        count += 1
print(count)
    
pos = 1
for j in percent:
    if j >= requirement: # pass
        print("{} {:.2f}".format(pos, j))
    else:
        print("({}) {:.2f}".format(pos, j))
    pos += 1
