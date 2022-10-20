def count_char(word):
    count = {}
    w_low = word.lower()

    for i in w_low:
        if i.isalpha():
            count[i.lower()] = 0
            
    for j in w_low:
        if j in count:
            count[j] += 1
    return count