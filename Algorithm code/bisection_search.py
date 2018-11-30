def divide_half(list):
    n = len(list)//2
    first_half = (list[:n])
    second_half = (list[n:])
    return first_half,second_half
divide_half([1,2,3,4,5,6,7])
from merge_sort import mergeSort as ms
def bisection_search(list,ele):
    list = ms(list)
    start = 0
    middle = len(list)//2
    end  = len(list)
    while ele < list[len(list)//2]:
        list = divide_half(list)[0]
    else:
        list = divide_half(list)[1]
        if len(list)== 1:
            if ele == list[0]:
                return True
            else:
                return False
print(bisection_search([1,2,3,4,5,6],3))

         

