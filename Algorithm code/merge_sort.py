def mergeSort(arr):
    if len(arr) == 1:
        return arr
    else:
        a = arr[:len(arr)//2]
        b = arr[len(arr)//2:]
        a = mergeSort(a)
        b = mergeSort(b)
        c = []
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                c.append(a[i])
                i = i + 1
            else:
                c.append(b[j])
                j = j + 1        
        c += a[i:]
        c += b[j:]
        # print('c= ',c)
    return c
def old_sort(arr):
    tg = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                tg = arr[i]
                arr[i]=arr[j]
                arr[j] = tg     
    return arr


