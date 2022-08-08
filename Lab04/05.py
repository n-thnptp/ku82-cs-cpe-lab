age = int(input("Enter your age: "))
n_income = int(input("Enter your net income: "))


if 15 <= age <= 60 and 1 <= n_income <= 79999:
    if 1 <= n_income <= 30000:
        nit_20 = n_income * 20 / 100
        print("Your negative income tax is {:.2f} Baht.".format(nit_20))
    elif n_income > 30000:
        total = (n_income - 30000) * 12 / 100
        total_2 = (30000 * 20 / 100) - total
        print("Your negative income tax is {:.2f} Baht.".format(total_2))

elif age < 15 or age > 60:
    print("Invalid age.")

elif n_income < 0 or n_income > 79999:
    print("Invalid income.")