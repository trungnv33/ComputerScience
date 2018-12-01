def divide_half(list):
    n = len(list)//2
    first_half = (list[:n])
    second_half = (list[n:])
    return first_half,second_half
from merge_sort import mergeSort as ms
def bisection_search(list,ele):
    list = ms(list)
    i,j = 0,0
    while i<len(list) and j <len(list):
        i,j =  0, 0
        if ele<list[len(list)//2]:
            list = divide_half(list)[0]
            i+=1
        else:
            list = divide_half(list)[1]
            j+=1
        print(list)
    if ele == list[0]:
        return True
    else:
        return False


         

