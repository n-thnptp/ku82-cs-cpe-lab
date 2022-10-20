msg = input()
vowels = "aeiou"
c_vowels = "AEIOU"

output = ""
for i in msg:
    if i in vowels or i in c_vowels:
        output += i.upper()
    else:
        output += i.lower()
        
print(output)