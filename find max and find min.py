def find_min(list):
    index = 1
    min = list[0]
    
    while index < len(list):
        if min > list[index]:
            min = list[index]
        index = index + 1
    
    return min


e = find_min([200, 300])
print(e)