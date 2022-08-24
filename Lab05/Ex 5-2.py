nums = []
i = 0
while True:
    f_input = input()

    if (len(f_input) > 0) and (f_input != " "):

        f_input = float(f_input)
        nums.append(f_input)
        i += 1

    else:

        break

avg = sum(nums) / i

print("{:.2f} {:.2f}".format(max(nums), min(nums)))
print("{:.2f} {:.2f}".format(sum(nums), avg))
