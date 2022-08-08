length = int(input("Enter block length: "))
width = int(input("Enter block width: "))
hlength = int(input("Enter house length: "))
hwidth = int(input("Enter house width: "))

lw = length * width
hlw = hlength * hwidth
total = (lw - hlw) * 35

print("Mowing cost is", total, "baht.")

input()