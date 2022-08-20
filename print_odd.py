# print all the odd numbers in a list
def print_odd_num(list):
    index = 0
    
    while index < len(list):
        if list[index] % 2 == 1:
            print(list[index])
            
        index = index + 1
        
        
        
list = [1, 2, 3, 4, 5, 6, 7]
print_odd_num (list)