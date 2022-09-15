def remove_duplicates(t):
    output = []
    for i in t:
        if i not in output:
            output.append(i)
            
    return output

print(remove_duplicates([1, 2, 3, 2, 1, 2, 3, 4]))
print(remove_duplicates(['a', 'b', 'c', 'e', 'f']))
print(remove_duplicates([2, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3]))
print(remove_duplicates([]))