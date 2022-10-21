def get_assignment(a_amount):               # assignment amount
    a_amount = a_amount.split(" ")
    return [int(a) for a in a_amount]

def get_criteria(criteria):                # [attendant, assignment success rate]
    criteria = criteria.split(" ")
    return [float(s) for s in criteria]

assignment = input()
assignment_out = get_assignment(assignment)
crit = input()
crit_out = get_criteria(crit)
students = int(input())

# attendance
att_dict = {}
for i in range(1, students+1):
    att = input()
    att = att.split(" ")
    att_dict[i] = att

for key in att_dict:
    missed = att_dict[key].count("0")
    percentage = 100 - ((missed*100)/len(att_dict[key]))
    att_dict[key] = percentage
    
# assignments
asm_dict = {}
for j in range(1, students+1):
    asm = input()
    asm = asm.split(" ")
    asm_dict[j] = sum([int(a) for a in asm])
    
for score in range(1, len(asm_dict)+1):
    asm_dict[score] = (asm_dict[score] / sum(get_assignment(assignment))) * 100

# result // "keys", "att_dict", "asm_dict"
result = {}
failed = 0
for r in range(1, students+1):
    result[r] = att_dict[r], asm_dict[r]
    
for f_keys, f_val in result.items():
    if f_val[0] < crit_out[0] and f_val[1] < crit_out[1]:
        failed += 1
    
print(failed)
for r_keys, r_val in result.items():
    if r_val[0] < crit_out[0] and r_val[1] < crit_out[1]:
        print("({}) {:.2f} {:.2f}".format(r_keys, r_val[0], r_val[1]))
    else:
        print("{} {:.2f} {:.2f}".format(r_keys, r_val[0], r_val[1]))