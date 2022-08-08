b_choice = input("Enter your buffet choice: ")

# pricing
jp_buffet = 1000
kr_buffet = 1500

if b_choice == "Korean" or b_choice == "Japanese":
    
    today = input("Is today Wednesday (yes/no)? ")

    # buffet choice "Korean"
    if b_choice == "Korean":
        if today == "yes":
            total = kr_buffet - (kr_buffet * 15 / 100)
            y_output = "Your payment is {:.2f} Baht.".format(total)
            print(y_output)
        elif today == "no":
            n_output = "Your payment is {:.2f} Baht.".format(kr_buffet)
            print(n_output)

    # buffet choice "Japanese"
    elif b_choice == "Japanese":
        if today == "yes":
            total = jp_buffet - (jp_buffet * 15 / 100)
            y_output = "Your payment is {:.2f} Baht.".format(total)
            print(y_output)
        elif today == "no":
            n_output = "Your payment is {:.2f} Baht.".format(jp_buffet)
            print(n_output)

else:
    output = "Sorry, there is no {} buffet.".format(b_choice)
    print(output)