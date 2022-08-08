# main menu
print("---<< Main Menu >>---")
b = "{s:>4s}<B>urger Meal".format(s = "")
c = "{s:>4s}<C>hicken Meal".format(s = "")
p = "{s:>4s}<P>asta Meal".format(s = "")
print(b)
print(c)
print(p)

choice = input("Enter your choice: ") # enter first choice

# if choice b is selected then
if choice == "b" or choice == "B":
    print("---<< Burger Sub Menu >>---")
    burger_r = "{s:>4s}<R>egular Burger".format(s = "")
    burger_c = "{s:>4s}<C>heese Burger".format(s = "")
    burger_d = "{s:>4s}<D>ouble Cheese Burger".format(s = "")
    print(burger_r)
    print(burger_c)
    print(burger_d)

    sub_choice = input("Enter your choice: ") # enter sub-menu choice

    if sub_choice == "r" or sub_choice == "R":
        print("Your Regular Burger is 60 Baht.")
    elif sub_choice == "c" or sub_choice == "C":
        print("Your Cheese Burger is 75 Baht.")
    elif sub_choice == "d" or sub_choice == "D":
        print("Your Double Cheese Burger is 90 Baht.")
    else:
        print("Invalid sub menu choice.")

# if choice c is selected then
elif choice == "c" or choice == "C":
    print("---<< Chicken Sub Menu >>---")
    chic_f = "{s:>4s}<F>ried Chicken".format(s = "")
    chic_g = "{s:>4s}<G>rilled Chicken".format(s = "")
    chic_c = "{s:>4s}<C>hef's Chicken".format(s = "")
    print(chic_f)
    print(chic_g)
    print(chic_c)

    sub_choice = input("Enter your choice: ") # enter sub-menu choice

    if sub_choice == "f" or sub_choice == "F":
        print("Your Fried Chicken is 120 Baht.")
    elif sub_choice == "g" or sub_choice == "G":
        print("Your Grilled Chicken is 150 Baht.")
    elif sub_choice == "c" or sub_choice == "C":
        print("Your Chef's Chicken is 180 Baht.")
    else:
        print("Invalid sub menu choice.")

# if choice p is selected then
elif choice == "p" or choice == "P":
    print("---<< Pasta Sub Menu >>---")
    pas_s = "{s:>4s}<S>paghetti de Italiano".format(s = "")
    pas_l = "{s:>4s}<L>asagna Supreme".format(s = "")
    pas_m = "{s:>4s}<M>acaroni Special".format(s = "")
    print(pas_s)
    print(pas_l)
    print(pas_m)

    sub_choice = input("Enter your choice: ") # enter sub-menu choice

    if sub_choice == "s" or sub_choice == "S":
        print("Your Spaghetti de Italiano is 90 Baht.")
    elif sub_choice == "l" or sub_choice == "L":
        print("Your Lasagna Supreme is 120 Baht.")
    elif sub_choice == "m" or sub_choice == "M":
        print("Your Macaroni Special is 100 Baht.")
    else:
        print("Invalid sub menu choice.")

# if none of the condition matches then
else:
    print("Invalid main menu choice.")