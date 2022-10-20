def create_table(mn):
    mn = mn.split("x")

    m = int(mn[0])
    n = int(mn[1])
    print([[0] * n] * m)
        
get_mn = input()
table = create_table(get_mn)

print(table[0][1])