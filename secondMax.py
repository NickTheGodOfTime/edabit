def second_max(list):
    index = 1
    maxn = list[0]
    lastMax = -1
    
    while index < len(list):
        if maxn > list[index]:
            lastMax = max
            maxn = list[index]
            
        elif lastMax < list[index]:
            lastMax = list[index]
        
        index = index + 1
        
    
    return lastMax


max = second_max([5, 6, 99, 10, 3, 67, 45, 112])
print(max)

max = second_max([5, 6, 99, 10, 3, 67, 45, 112, 100])
print(max)
