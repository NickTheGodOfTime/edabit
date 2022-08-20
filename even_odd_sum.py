def even_odd_sum(list):
    index = 0
    sumodd = 0
    sumeven = 0
    
    while index < len(list):
        if list[index] % 2 == 1:
            sumodd = sumodd + list[index]   
        else:
            sumeven = sumeven + list[index]
              
        index = index + 1
        
    return sumeven - sumodd

e = even_odd_sum([1, 2, 3, 4, 5])
print(e)