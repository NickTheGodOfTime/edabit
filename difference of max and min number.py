def difference_max_min(list):
    difference = max(list) - min(list)
    return difference


e = difference_max_min([10, 4, 1, 4, -10, -50, 32, 21])
print(e)
e = difference_max_min([44, 32, 86, 19])
print(e)