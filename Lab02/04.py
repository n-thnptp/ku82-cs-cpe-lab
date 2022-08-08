# input
print("First fraction:")
a = int(input(">>Enter a numerator a: "))
b = int(input(">>Enter a denominator b: "))
print("Second fraction:")
c = int(input(">>Enter a numerator c: "))
d = int(input(">>Enter a denominator d: "))

# process
p = a * d + b * c
q = b * d

# output
print("Summation of the two fractions is %d / %d" %(p, q)) 