bid_dict = {}
while True:
    bidders = input()
    if bidders == "end":
        break
    bidders = bidders.split(" ")
    
    count = 1
    if bidders[0] not in bid_dict:
        bid_dict[bidders[0]] = [int(bidders[1]), count]
    else:
        count = bid_dict[bidders[0]][1] + 1
        if int(bidders[1]) > bid_dict[bidders[0]][0]:
            bid_dict[bidders[0]][0] = int(bidders[1])
            bid_dict[bidders[0]][1] = count
        else:
            bid_dict[bidders[0]][1] = count

for result in sorted(bid_dict):
    if bid_dict[result][1] > 1:
        print("{} bid at the price of {:.1f} baht in {} times.".format(result, bid_dict[result][0], bid_dict[result][1]))
    else:
        print("{} bid at the price of {:.1f} baht in {} time.".format(result, bid_dict[result][0], bid_dict[result][1]))
price = []
times = []
for p in sorted(bid_dict):
    price.append(bid_dict[p][0])
    times.append(bid_dict[p][1])

for w in bid_dict:
    if bid_dict[w][0] == max(price) and bid_dict[w][1] == min(times):
        print("The winner is {}.".format(w))
        break