def filter_factors_3_7(ls):
    factor = []
    output = []
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            factor.append(i)

    for j in factor:
        if j in ls:
            ls.remove(j)
    
    output.append(factor)
    output.append(ls)
    return output

print(filter_factors_3_7([3, 7, 9, 10, 20, 50]))