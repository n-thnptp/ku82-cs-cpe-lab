def namelist(names):
    joined = ", ".join(names)
    last = joined.rfind(",")

    replace = " &"
    for i in range(len(joined)):
        if i == last:
            joined = joined[:i] + replace + joined[i+1:]
    return joined