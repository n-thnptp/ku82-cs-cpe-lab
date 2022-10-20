ls = []
while True:
    delimeter = input()
    if delimeter == "":
        break
    else:
        ls.append(delimeter)
ls = ",".join(ls)
print(ls)