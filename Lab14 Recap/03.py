notes = input().split(",")
n = int(input())
# check1 = len(notes)

count = 0
i = 0
while True:
    # current = notes[i]
    if count == n:
        print(notes[i-1])
        break
    if i == len(notes)-1:
        i = 0
        continue    
    i += 1
    count += 1