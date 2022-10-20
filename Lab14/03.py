var = {}
prog = []

print("Enter variables and values:")
while True:
    var_val = input()
    
    if var_val == "-1":
        break
    else:
        split = var_val.split("=")
        var[split[0].strip()] = split[1].strip()
        
print("Enter your program:")
while True:
    prog_in = input()
    
    if prog_in == "-1":
        break
    else:
        prog.append(prog_in)
        
print("Result:")
v_keys = list(var.keys())
output = []
z = ""
for p in prog:
    for keys in v_keys:
        if z == "":
            z = p.replace("{"+keys+"}", str(var.get(keys)))
            if z.find("{") == -1 and z not in output:
                output.append(z)
        else:
            z = z.replace("{"+keys+"}", str(var.get(keys)))
            if z.find("{") == -1 and z not in output:
                output.append(z)
    z = ""
    
for o in output:
    print(o)