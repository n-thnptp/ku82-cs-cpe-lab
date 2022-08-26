# Enter height: 5
#         1         (mid 0) i = 0 
#       1   1       (mid 3) i = 1 
#     1       1     (mid 7) i = 2
#   1           1   (mid 11) i = 3
# 1               1 (mid 15) i = 4

height = int(input("Enter height: "))

s = 2
i = 0
while i < height:
    print((" " * ((height*2) - s)) + "1", end = "")
    
    if i >= 1:
        print((" " * ((i * 4) - 1) + "1"), end = "")
    print()
    
    s += 2
    i += 1
