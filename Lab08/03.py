def simple_interest(p, r, t):
    interest = (p * r * t)/100
    total = interest + p
    return total

def compound_interest(p, r, t):
    c_interest = (p * ((1 + r/100) ** t))
    total = c_interest + p
    return total

p = int(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))
print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))