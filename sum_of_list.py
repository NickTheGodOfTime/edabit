# write a function which
# gives the sum of all the elements in a list
def sum_of_list(list):
    # intial value
    # condtion
    # a way to break the condition
    sum = 0
    index = 0
    
    while index < len(list):
        sum = sum + list[index]
        index = index + 1
        
    return sum
    

e = sum_of_list([1, 2, 3])
print (e)
# should print 6