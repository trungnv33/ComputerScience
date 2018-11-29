def old_sort(arr):
    tg = 0
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                tg = arr[i]
                arr[i]=arr[j]
                arr[j] = tg     
    return arr