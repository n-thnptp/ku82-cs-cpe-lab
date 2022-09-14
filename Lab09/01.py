def check_prime(n):
    if n > 1:
        i = 2
        while i < n:
            if (n % i) == 0:
                return False
            i += 1
        return True
    else:
        return False
    
n = int(input("Enter number: "))
if check_prime(n):
    print(n,"is a prime number.")
else:
    print(n,"is not a prime number.")