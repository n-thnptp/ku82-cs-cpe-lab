dis = int(input()) # distance
cap = int(input()) # capacity

kaew = (15 * cap/2)
kwan = (15 * cap*9/10)

kaew_cal = 1 + dis / kaew
kwan_cal = 1 + dis / kwan

print(int(kaew_cal))
print(int(kwan_cal))