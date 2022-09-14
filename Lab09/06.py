# เช่น Alternating Sum ของ 10 จำนวนแรก คือ 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10 = -5

# Alternating Sum ของ 15 จำนวนแรก คือ 1 - 2 + 3 - 4 + 5 - 6 + 7 - 8 + 9 - 10 + 11 - 12 + 13 - 14 + 15 = 8

# 0+1   (1) i + j
# 1

# 1-2   (2) i - j
# -1

# -1+3  (3)
# 2

# 2-4   (4)
# -2

# -2+5  (5)
# 3

# 3-6   (6)
# -3

# -3+7  (7)
# 4

# 4-8   (8)
# -4

# -4+9  (9)
# 5

# 5-10  (10)
# -5

def alt_sum(n):
    i = 1
    num1 = 0
    num2 = 1

    while i <= n:
        if (i % 2) != 0:
            # +
            num1 = num1 + num2
        else:
            # -
            num1 = num1 - num2
        i += 1
        num2 += 1
        
    return num1

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n, alt_sum(n)))