n = int(input())
sym = input()
fibo = []
flag = False

for i in range(n+1):
    if i == 0 or i == 1:
        fibo.append(1)
    else:
        calc = fibo[i-2] + fibo[i-1]
        fibo.append(calc)
    
output = 0
if sym in ['e', 'E']:
    for j in range(len(fibo)):
        if j % 2 == 0:
            output += fibo[j]
            flag = True
elif sym in ['o', 'O']:
    for k in range(len(fibo)):
        if k % 2 != 0:
            output += fibo[k]
            flag = True
            
if flag == False:
    print("ERROR")
else:
    print(output)