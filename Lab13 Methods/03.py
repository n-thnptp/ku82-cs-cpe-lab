def filter_sort_factors_3_7(ls):
    factor = []
    non_factor = []
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            factor.append(i)
        elif i % 3 != 0 and i % 7 != 0:
            non_factor.append(i)
    factor.sort()
    non_factor.sort(reverse=True)
    output = []
    output.append(factor)
    output.append(non_factor)
    return output

print(filter_sort_factors_3_7([3, 7, 9, 10, 20, 50]))