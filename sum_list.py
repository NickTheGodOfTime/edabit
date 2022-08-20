def sum_list(list):
    index = 0
    sumList = 1
    
    while index < len(list):
        sumList = sumList + list[index]
        index = index + 1
    
    return sumList

e = sum_list([1, 2, 3, 4])
print(e)