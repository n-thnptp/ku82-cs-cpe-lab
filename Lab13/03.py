n = int(input())
bn = []
for i in range(n):
    m = int(input())
    bn.append(m)
bn.sort(reverse=True)

change = int(input())
total = 0
n = 0
c_cash = []
for j in bn:
    while n < len(bn):
        if total + bn[n] <= change:
            c_cash.append(bn[n])
            total += bn[n]
        else:
            n += 1
    if total == change:
        break
        
for cash in bn:
    print("{}: {}".format(cash, c_cash.count(cash)))