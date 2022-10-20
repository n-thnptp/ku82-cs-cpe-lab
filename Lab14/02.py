def cloth_size(width_list):
    size = {'S': 0, 'M': 0, 'L': 0}

    for i in width_list:
        if i <= 36:
            size['S'] += 1
        elif i >= 36 and i <= 44:
            size['M'] += 1
        elif i > 44:
            size['L'] += 1
            
    return size