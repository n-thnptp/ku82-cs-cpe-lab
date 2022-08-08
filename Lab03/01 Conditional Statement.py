dc = float(input())
sym = str(input())

if sym == 'F' or sym == 'f':
    print(9/5 * dc + 32)
elif sym == 'K' or sym == 'k':
    print(dc + 273.15)
else:
    print("ERROR")