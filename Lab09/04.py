def factorial(n):
    result = 1
    i = 1
    if n == 1:
        result == 1
    else:
        while i <= n:
            result *= i
            i += 1
    return result

n = int(input("Enter n: "))
print("{}!".format(n), "=", factorial(n))