def create_table(get_mn):             # used to create table
    get_mn = get_mn.split("x")
    m = int(get_mn[0])          # rows
    n = int(get_mn[1])          # column
    ls = []
    
    for i in range(m):
        ls.append([0]*n)
            
    return ls

def changeToInt(x):
    split = x.split("x")
    m = int(split[0])
    n = int(split[1])
    ls_mn = [m, n]
    
    return ls_mn
    
get_mn = input()
mn = changeToInt(get_mn)
ls = create_table(get_mn)

bomb_ls = []                            # [[rows, column], [rows, column], ...]
n_bomb = int(input())
for i in range(n_bomb):
    add = []
    pos = input().split(",")
    for j in pos:
        add.append(int(j))
    bomb_ls.append(add)
    
for bpos in bomb_ls:
    r = bpos[0]
    c = bpos[1]
    if (r >= 0 and r <= mn[0]) and (c >= 0 and r <= mn[1]):
        for ra in range(len(ls)):           # for rows
            for ca in range(len(ls[ra])):   # for column
                if (ra == r and ca == c) and (ls[r][c] != "*"):
                    # if the current place is not "*" then +1
                    # and if the current row and column is inside the table then change
                        ls[r][c] = "*"
                        if r+1 <= mn[0]-1 and c+1 <= mn[1]:
                            if ls[r][c-1] != "*" and c-1 >= 0:
                                ls[r][c-1] += 1
                            if ls[r][c+1] != "*" and c+1 <= mn[1]:
                                ls[r][c+1] += 1
                            if ls[r-1][c] != "*" and r-1 >= 0:
                                ls[r-1][c] += 1
                            if ls[r-1][c-1] != "*" and (r-1 >= 0 and c-1 >= 0):
                                ls[r-1][c-1] += 1
                            if ls[r-1][c+1] != "*" and (r-1 >= 0 and c+1 <= mn[1]):
                                ls[r-1][c+1] += 1
                            if ls[r+1][c] != "*" and (r+1 <= mn[0]):
                                ls[r+1][c] += 1
                            if ls[r+1][c-1] != "*" and (r+1 <= mn[0] and c-1 >= 0):
                                ls[r+1][c-1] += 1
                            if ls[r+1][c+1] != "*" and (r+1 <= mn[0] and c+1 <= mn[1]):
                                ls[r+1][c+1] += 1
            
for o in ls:
    s = ""
    for o1 in o:
        s += str(o1)
    print("{}".format(s))