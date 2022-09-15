import math

def find_sd(l):                     #find standard deviation
    n = len(l)
    mean = sum(l) / n
    sum_score = 0
    for x in l:
        sum_score += (x - (mean)) ** 2
    var = math.sqrt(sum_score / (n-1))
    return var

score_list = []
while True:
    score = float(input("Enter score: "))
    if score == -1:
        break
    elif score > 100 or score < 0:
        print("Score is out of range.")
    else:
        score_list.append(score)

if score_list != []:

    avg = sum(score_list) / len(score_list)
    
    print("Maximum score is {:.2f}.".format(max(score_list)))
    print("Minimum score is {:.2f}.".format(min(score_list)))
    print("Average score is {:.2f}.".format(avg))
    print("Standard deviation is {:.2f}.".format(find_sd(score_list)))