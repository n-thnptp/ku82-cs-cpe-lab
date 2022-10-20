# 5
# 3, 6, 7, 9, 12

def create_factors_3_7(n):
    ls = []

    count = 0
    i = 3
    while len(ls) < n:
        if i % 3 == 0 or i % 7 == 0:
            ls.append(i)
        i += 1
        count += 1
    return ls

print(create_factors_3_7(5))