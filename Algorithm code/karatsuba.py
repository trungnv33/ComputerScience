# def multiply(a,b):
#     if b==1 :
#         return a
#     if a== 0 or b==0:    
#         return 0
#     else:
#         return a + multiply(a,b-1)
# def half_divided(var):
#     n = len(str(var))
#     var_1 = var//(10**(n//2))
#     var_2 = var%(10**(n//2))
#     return var_1,var_2
def product(x,y):
    n =(len(str(x)))
    if n <= 1:
        return x*y
    else:
        a,b = x//(10**(n//2)),x%(10**(n//2))
        c,d = y//(10**(n//2)),y%(10**(n//2))
        p = a+b
        q = c+d
        ac = product(a,c)
        bd = product(b,d)
        pq = product(p,q)
        adbc = pq-ac-bd
        result = 10**n * ac + (10**(n//2)) *adbc+bd
        return result
print(product(567,123))
