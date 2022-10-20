chem = input()
find = input()

chem_dict = {}
keys_split = ""
val_in = 0
for i in range(len(chem)):          # split input into chunks (eg. Fe3-H2-Na2-...)
    keys_split += chem[i]
    if i+1 < len(chem):
        if chem[i+1].isupper():
            keys_split += "-"
keys_split = keys_split.split("-")

for j in keys_split:               # assign them to dict as chem_dict[keys] = values
    keys = ""
    vals = ""
    for k in j:
        if k.isalpha():            # for keys
            keys += k
        else:                      # for values
            vals += k
    if vals == "":
        chem_dict[keys] = "1"
    else:
        chem_dict[keys] = vals

if find not in chem_dict:
    print("0")
else:
    print(chem_dict.get(find))