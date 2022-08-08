import math

x = float(input("Enter x : "))

if x < 0:
    case1 = math.sqrt((x**2) + 1)
    case1_a = math.ceil(case1)
    print(f"f({x:.2f}) = {case1_a}")

elif x == 0:
    case2 = math.ceil(x)
    print(f"f({x:.2f}) = {case2}")

elif 0 < x <= 99:
    case3 = (3 * (x**2)) - (1 - x)**2
    case3_a = math.ceil(case3)
    print(f"f({x:.2f}) = {case3_a}")

elif x > 99:
    case4 = (2 * (x**3)) - (x / math.sqrt(x+1))
    case4_a = math.ceil(case4)
    print(f"f({x:.2f}) = {case4_a}")
