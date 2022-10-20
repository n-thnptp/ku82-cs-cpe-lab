# rows = 5
# |    *    | i = 0
# |   ***   | i = 1
# |  *****  | i = 2
# | ******* | i = 3
# |*********| i = 4

rows = int(input())

j = rows-1
s = 1
for i in range(1, rows+1):
    print("|" + " "*j + "*"*s + " "*j + "|")
    j -= 1
    s += 2