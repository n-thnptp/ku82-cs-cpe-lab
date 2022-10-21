def extract_string(text):
    if text == "":
        return []
    flag = "alpha"                  # check for the FIRST iteration if it is alphabet or digits
    if text[0].isdigit():           # then set the flag
        flag = "digit"
        
    ext = ""
    j = 0
    for i in range(len(text)):
        ext += text[i]              # add current iteration to new variable "ext"
        if i+1 < len(text):         # check if the next iteration is digit or alphabet
            if text[i+1].isdigit() and flag == "alpha":
                ext += "_"
                flag = "digit"
            if text[i+1].isdigit() == False and flag == "digit":
                ext += "_"
                flag = "alpha"
            
    ext = ext.split("_")           # split the extracted text
    
    for j in range(len(ext)):      # turn string to int if it is a digit
        if ext[j].isdigit():
            ext[j] = int(ext[j])
            
    return ext                     # return result

print( extract_string("G2X3t4") )
print( extract_string("AB12XY23") )
print( extract_string("Number 4, Privet Drive") )
print( extract_string("1 2 3 4 5 I love you.") )
print( extract_string(""))