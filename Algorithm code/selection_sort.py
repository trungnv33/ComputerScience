def find_min(arr):
    min = arr[0]
    length = len(arr)
    vi_tri = 0
    for i in range(0,length):
        if arr[i]<min:
            min = arr[i]
            vi_tri = i
    return min,vi_tri
def selection_sort(arr):
    var = 0
    while var <len(arr):
        min, vi_tri = find_min(arr[var:])
        vi_tri += var
        arr[vi_tri] = arr[var]
        arr[var] = min
        var +=1
        print(arr)
    return arr