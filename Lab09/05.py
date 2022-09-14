def fibo(n):
    n1, n2 = 0, 1
    if n == 1:
        n1 = 1
    elif n == 2:
        n1 = 1
    elif n > 2:
        i = 0
        while i < n:
            result = n1 + n2
            n1 = n2
            n2 = result
            i += 1
    return n1

n = int(input("Enter n: "))
print("fibo({}) = {}".format(n, fibo(n)))