def nb_year(p0, percent, aug, p):
    days = 0
    result = 0
    while result < p:
        b_amount = p0 + ((p0 * percent)//100) + aug
        result = b_amount
        p0 = b_amount
        days += 1
    return days

print(nb_year(1500000, 0.25, 1000, 2000000))
print(nb_year(1000, 2, 30, 1150))