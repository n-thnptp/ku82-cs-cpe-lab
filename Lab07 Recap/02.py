print("Upper left corner coordinate:")
x = float(input("  << x axis: "))
y = float(input("  << y axis: "))
east = float(input("  << Eastern: "))
south = float(input("  << Southern: "))

print("Enter a coordinate:")
xCoor = float(input("  << x axis: "))
yCoor = float(input("  << y axis: "))

x1 = x + east
y1 = y - south

if (x <= xCoor <= x1) and (y <= yCoor <= y1 or y >= yCoor >= y1):
    print(">>> ({:.2f}, {:.2f}) is inside the rectangle.".format(xCoor, yCoor))
else:
    print(">>> ({:.2f}, {:.2f}) is not inside the rectangle.".format(xCoor, yCoor))