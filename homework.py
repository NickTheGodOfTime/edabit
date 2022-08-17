# product of list 
# print all the element of the list
def product_of_a_list(list):
    product = 1
    indexOfList = 0
    
    while indexOfList < len(list):
        product = product * list[indexOfList]
        indexOfList = indexOfList + 1
    
    return product


e = product_of_a_list([2, 2, 3, 4, 5])
print(e)

def elements_of_a_list(list):
    index = 0
    while index < len(list):
        element = list[index]
        print (list[index])
        index = index + 1



d = elements_of_a_list([7, 10,  1, 2, 3, 4, 5])