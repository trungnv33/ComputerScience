def partition(string):
    if len(string) == 1:
        return string
    else:
        n = len(string)
        i = 0
        merge= ''
        first_half = string[:n//2]
        second_half = string[n//2:]
        while i<len(string):
            partition(first_half)
            c+ =first_half
            i+ =1
        else:
            partition(second_half)
        return merge
print(partition('trung'))