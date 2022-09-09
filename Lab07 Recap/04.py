import math

while True:
    print("<<Point a>>")
    x1 = int(input("Enter x coordinate: "))
    y1 = int(input("Enter y coordinate: "))
    print("<<Point b>>")
    x2 = int(input("Enter x coordinate: "))
    y2 = int(input("Enter y coordinate: "))

    dis = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))
    h_dis = math.fabs(x1 - x2)
    v_dis = math.fabs(y1 - y2)

    print("Distance between ({}, {}) and ({}, {}): ".format(x1, y1, x2, y2))
    print("Euclidean distance is {:.2f}.".format(dis))
    print("Horizontal distance is {}.".format(h_dis))
    print("Vertical distance is {}".format(v_dis))