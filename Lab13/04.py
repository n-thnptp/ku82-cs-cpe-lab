def get_date(date):
    ex_date = []
    split_d = date.split("-")
    
    for i in range(len(split_d)):
        if int(split_d[i]) < 10:
            ex_date.append(split_d[i][1])
        else:
            ex_date.append(split_d[i])
            
    return ex_date

# day - month

first_date = input()
second_date = input()
sunday = int(input())

dates = []
dates.append(get_date(first_date))
dates.append(get_date(second_date))

if (int(get_date(first_date)[1]) > 12) or (int(get_date(second_date)[1]) > 12):
    print("Wrong Month")
    if (int(get_date(first_date)[0]) > 31) or (int(get_date(second_date)[0]) > 31):
        print("Wrong Day")
elif (int(get_date(first_date)[0]) > 31) or (int(get_date(second_date)[0]) > 31):
    print("Wrong Day")