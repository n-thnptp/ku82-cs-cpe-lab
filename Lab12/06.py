# 1200 = 1200
# 123.45 = 124.45
# 4,200,257 = 4200258
# 1,200.50
# 13.456 = ERROR
# 1a.45 = ERROR
# 24.1346 = ERROR

alphabet = "abcdefghijklmnopqrstuvwxyz"
def checkNums(x):
    for i in x:
        if i in alphabet:
            return True
        
def checkLen(x):
    for i in range(len(nums)):
        if i == 0 and len(nums[i]) > 3:
            return True
        else:
            if i > 0 and len(nums[i]) != 3:
                return True

n = input()

if n.find(".") != -1 or n.find(",") != -1:
    if checkNums(n) == True:  # check if alphabet exists in the input
        print("ERROR")
        
    elif n.find(".") != -1:   # floats
        if len(n[n.find(".")+1:]) == 2:
            nums = int(n[:n.find(".")]) + 1
            floats = n[n.find(".")+1:]
            print("{}.{}".format(nums, floats))
        else:
            print("ERROR")
            
    elif n.find(",") != -1:   # nums
        output = ""
        nums = n.split(",")
        if checkLen(nums) == True:
            print("ERROR")
        else:
            for i in range(len(nums)):
                if i+1 == len(nums):
                    add_1 = int(nums[i]) + 1
                    output += str(add_1)
                else:
                    output += nums[i]
            print(output)
else:
    print(n)