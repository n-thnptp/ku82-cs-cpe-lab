score = 0
i = 1
while i <= 10:
    print("Frame # {}".format(i))
    pins = int(input("  Number of pins down: "))
    down = 10 - pins

    if pins != 10 and (pins >= 0 or pins <= 10):
        print("Frame # {}".format(i))
        secondPins = int(input("  Number of pins down (0-{}): ".format(down)))
        total = pins + secondPins
        if total == 10 and total >= 10:
            score += 10 # spare
        elif total != 10 and (total >= 0 or total <= 10):
            score += total
    else:
        score += 10

    i += 1
print("Total score is {}".format(score))