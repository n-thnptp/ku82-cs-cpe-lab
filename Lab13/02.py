n = int(input())
output = []

for i in range(n):
    cards = input()
    cards = cards.split()
    
    total = 0
    for j in range(len(cards)):
        if total > 16 or total > 21:
            break
        if cards[j] in ['J', 'Q', 'K']:
            total += 10
        if cards[j] == 'A':
            total += 1
        if cards[j].isdigit():
            total += int(cards[j])
    
    if total > 21:
        output.append("busted")
    else:
        output.append(total)
        
for o in output:
    print(o)