tv = int(input("How many TVs? "))
dvd_p = int(input("How many DVD players? "))
audio_sys = int(input("How many Audio Systems? "))

tv_n = tv * 6000
dvd_n = dvd_p * 1500
audio_n = audio_sys * 3000

total = tv_n + dvd_n + audio_n
total_output = "Total price is {:.2f} baht.".format(total)
print(total_output)

if total >= 24000:
    disc = total * 20 // 100 # discount
    disc_output = "You've got a discount of {:.2f} baht.".format(disc)
    print(disc_output)

    disc_payment = total - disc # total after discount
    payment_output = "Your payment is {:.2f} baht. Thank you!".format(disc_payment)
    print(payment_output)

elif total < 24000:
    payment_output = "Your payment is {:.2f} baht. Thank you!".format(total)
    print(payment_output)