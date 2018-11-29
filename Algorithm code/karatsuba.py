def product(x,y):
    if x < 10 :
        return x*y
    else:
        n = int(len(str(x))/2)
        a,b = x//(10**(n)),x%(10**(n))
        c,d = y//(10**(n)),y%(10**(n))
        p = a+b
        q = c+d
        ac = product(a,c)
        bd = product(b,d)
        pq = product(p,q)
        adbc = pq-ac-bd
        result = 10**2*n * ac + (10**(n)) *adbc+bd
        return result
print(product(123,10000))
