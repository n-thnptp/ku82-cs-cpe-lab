num = []
while True:
    n = input()
    
    if n == "":
        break
    else:
        num.append(float(n))
        
print(num.count(min(num)))