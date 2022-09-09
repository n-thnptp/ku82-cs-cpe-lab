def digit(n):
    digit = n % 10
    return digit

def tens(n):
    n //= 10
    tens = n % 10
    return tens

def hundreds(n):
    n //= 100
    hundreds = n % 10
    return hundreds

def thousands(n):
    n //= 1000
    thousands = n % 10
    return thousands

def sum_digits(n):
    sum_digits = (digit(n)) + (tens(n)) + (hundreds(n)) + (thousands(n))
    return sum_digits

n = int(input('Enter a nber (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))