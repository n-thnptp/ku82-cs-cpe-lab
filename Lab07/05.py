while True:
    n = int(input("Enter a number: "))
    if n == 0:
        print("End of program, goodbye.")
        break
        
    elif n <= 1:
        print("Invalid input, try again.")
    
    else:
        count = 0
        div = 1
        i = 0
        while i <= n:
            total = n % div

            if total == 0:
                count += 1
            div += 1
            i += 1
        if count > 2:
            print("{} is not a prime number.".format(n))
        elif count <= 2:
            print("{} is a prime number.".format(n))