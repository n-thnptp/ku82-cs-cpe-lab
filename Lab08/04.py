def read_hour():
    hour = int(input("Enter hour: "))
    if 0 <= hour <= 23:
        return hour
    else:
        return False
def read_minute():
    minute = int(input("Enter minute: "))
    return minute
def read_second():
    second = int(input("Enter second: "))
    return second
def to_seconds(hour, minute, second):
    convert = (hour * 3600) + (minute * 60) + second
    return convert

def time_elapsed(start_time, finish_time):
    elapsed = finish_time - start_time
    hour = elapsed // 3600
    minute = (elapsed % 3600) // 60
    second = (elapsed % 3600) % 60
    return ("{} hours {} minutes {} seconds.".format(hour, minute, second))

def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)


print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))