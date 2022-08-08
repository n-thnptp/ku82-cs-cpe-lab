# input
s1 = int(input("Enter your exercise time 1: "))
s2 = int(input("Enter your exercise time 2: "))

# process
total = s1 + s2
h = total // 3600
mod_h = total % 3600 # remainder of total
m = mod_h // 60
s = total % 60

# output
print("It is", h, "hours", m, "minutes", s, "seconds.")


input("Enter to exit...")
