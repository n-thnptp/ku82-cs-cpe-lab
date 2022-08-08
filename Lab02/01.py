# import math module
import math

# input
r = float(input("Enter a radius: "))

# process
area = math.pi * r * r # find area
c_r = 2 * math.pi * r # find circumference of radius

# output
print("Area of a circle with radius %d is %.2f" %(r, area))
print("Circumference of a circle with radius %d is %.2f" %(r, c_r))

input()