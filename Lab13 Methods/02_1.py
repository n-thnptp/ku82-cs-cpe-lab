def count_factors_3_7(ls):
    output = []
    for i in ls:
        if i % 3 == 0 or i % 7 == 0:
            output.append(i)
    
    return len(output)