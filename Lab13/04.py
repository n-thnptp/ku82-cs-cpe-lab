dim = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]       # num of days from jan to dec
def changeToInt(date):
    done_ls = []
    split_d = date.split("-")
    
    for i in range(len(split_d)):
        done_ls.append(int(split_d[i]))
            
    return done_ls

def get_date(date):
    split_d = date.split("-")
    ex_date = [int(split_d[0]), int(split_d[1])]
    
    return sum(dim[1:ex_date[1]]) + ex_date[0]

# day - month
first_date = input()
second_date = input()
counter = int(input())
fd = changeToInt(first_date)
sd = changeToInt(second_date)

dates = []
dates.append(get_date(first_date))
dates.append(get_date(second_date))
dates.sort()

if (fd[1] > 12) or (fd[1] < 1) or (sd[1] > 12) or (sd[1] < 1):
    print("Wrong Month")
    if (fd[0] > 31) or (sd[0] > 31):
        print("Wrong Day")
elif (fd[0] > 31) or (sd[0] > 31) or (fd[0] > dim[fd[1]] or sd[0] > dim[sd[1]]):
    print("Wrong Day")
else:
    count_sun = 0
    while counter <= dates[1]:
        if counter >= dates[0] and counter <= dates[1]:
            count_sun += 1
        counter += 7
                
    print(count_sun)