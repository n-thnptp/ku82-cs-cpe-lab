p_level = int(input("Enter level pokemon: "))
pokeball = input("Enter level pokeball: ")
dist = int(input("Enter distance: "))

if pokeball == "H" or pokeball == "h":
    if 0 <= p_level <= 40:
        success_rate = 100 - (p_level * dist * 0.01)
    elif 41 <= p_level <= 60:
        success_rate = 100 - (p_level * dist * 0.01)
    elif 61 <= p_level <= 100:
        success_rate = 100 - (p_level * dist * 0.01)

    if 0 <= success_rate <= 100:
        print("{:.2f} percent.".format(success_rate))
    elif success_rate < 0:
        print("0.00 percent.")
    elif success_rate > 100:
        print("100.00 percent.")


elif pokeball == "M" or pokeball == "m":
    if 0 <= p_level <= 40:
        success_rate = 100 - (p_level * dist * 0.03)
    elif 41 <= p_level <= 60:
        success_rate = 100 - (p_level * dist * 0.05)
    elif 61 <= p_level <= 100:
        success_rate = 100 - (p_level * dist * 0.08)

    if 0 <= success_rate <= 100:
        print("{:.2f} percent.".format(success_rate))
    elif success_rate < 0:
        print("0.00 percent.")
    elif success_rate > 100:
        print("100.00 percent.")

elif pokeball == "L" or pokeball == "l":
    if 0 <= p_level <= 40:
        success_rate = 100 - (p_level * dist * 0.05)
    elif 41 <= p_level <= 60:
        success_rate = 100 - (p_level * dist * 0.03)
    elif 61 <= p_level <= 100:
        success_rate = 100 - (p_level * dist * 0.1)
    
    if 0 <= success_rate <= 100:
        print("{:.2f} percent.".format(success_rate))
    elif success_rate < 0:
        print("0.00 percent.")
    elif success_rate > 100:
        print("100.00 percent.")