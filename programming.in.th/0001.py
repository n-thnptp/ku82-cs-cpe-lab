score = int(input())
mid = int(input())
final = int(input())

if (score > 30 or score < 0) or (mid > 30 or mid < 0) or (final > 40 or final < 0):
    print("Invalid score.")
else:
    total = score + mid + final

    if total >= 80 and total <= 100:
        print("A")
    elif total >= 75 and total <= 79:
        print("B+")
    if total >= 70 and total <= 74:
        print("B")
    if total >= 65 and total <= 69:
        print("C+")
    if total >= 60 and total <= 64:
        print("C")
    if total >= 55 and total <= 59:
        print("D+")
    elif total >= 50 and total <= 54:
        print("D")
    elif total >= 0 and total <= 49:
        print("F")