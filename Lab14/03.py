var = {}
program = []

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
    program_in = input()
    
    if program_in == "-1":
        break
    else:
        program.append(program_in)
        
print("Result:")
for p in program:
    for key, value in var.items():              # eg. dict_items([('x', '5'), ('y', '6')])
        p = p.replace("{"+key+"}", value)       # assigned [('key', 'value')]
    print(p)