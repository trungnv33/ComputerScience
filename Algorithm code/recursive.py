def pow(a,n):
    if n == 0:
        return 1
    if n == 1:
        return a
    if n > 1: 
        return pow(a,n-1)*a
    else: 
        return 1/(pow(a,-n))
