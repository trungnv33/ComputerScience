def swap(a,b):
    tg  = 0
    tg = a
    a = b
    b = tg
    return a,b
def check(arr):
    boolean = True
    for i in range(len(arr)-1):
        if arr[i+1]<arr[i]:
            boolean = False
    return boolean
def bubble_sort(arr):
    i = 0
    boo = False
    while boo == False:
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                arr[i],arr[i+1] = swap(arr[i],arr[i+1])
            boo = check(arr)
    return arr
print(bubble_sort([1,3,2,0,1,2,10232,3,12,3,3,1232,13,131,1]))