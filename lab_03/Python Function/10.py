def uniq(lst):
    uniq_list = []
    for item in lst:
        if item not in uniq_list:
            uniq_list.append(item)
    return uniq_list

print(uniq([1, 2, 3, 3, 2, 1, 4, 5]))
print(uniq([7, 8, 8, 9, 10, 10, 7]))
print(uniq([]))
print(uniq([1, 1, 1, 1]))