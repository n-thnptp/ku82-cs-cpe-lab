n = int(input("Enter positive integer: "))

if n <= 0:
    print("Invalid number.")
else:
    prime = 2
    while n % 2 == 0:
        print(prime)
        n //= 2
        
    i = 3
    while n % i == 0:
        print(i)
        n //= i
        i += 2
        
    if n > 2:
        print(n)