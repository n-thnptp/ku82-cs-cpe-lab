# input
inc = float(input())
ex = float(input())
prof = inc + ex

# output
print("1234567890" * 3)

output = "Total Income {:>+8.2f} bahts\nExpense {:>13.2f} bahts\nProfit {s:>6}{:0>8.2f} bahts".format(inc, ex, prof, s="")
print(output)

# output = "Total Income +{a:>.2f} bahts\nExpense {b:>12.2f} bahts\nProfit {s:>5}{c:0>8.2f} bahts".format(a=inc, b=ex, c=prof, s="")
# print(output)

# print(f"{'Expense':<0}{ex:>14}{' bahts':>0}")
# print(f"{'Profit':<0}{0:>8}{prof:>07.2f}{' bahts':>0}")