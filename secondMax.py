def second_max(list):
    index = 1
    max = list[0]
    secondMax = -1
    
    while index < len(list):
        if max > list[index]:
            secondMax = max
            max = list[index]
            
        elif secondMax < list[index]:
            secondMax = list[index]
        
        index = index + 1
        
    
    return secondMax


max = second_max([5, 6, 99, 10, 3, 67, 45, 112])
print(max)

max = second_max([5, 6, 99, 10, 3, 67, 45, 112, 100])
print(max)
