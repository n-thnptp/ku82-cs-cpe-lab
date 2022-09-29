freq_list = []
for n in score_list:
    count = score_list.count(n)
    freq = 0
    if count >= freq:
        freq = count
        freq_list.append(n)
        
print(freq_list)