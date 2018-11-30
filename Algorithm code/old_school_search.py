def old_search(list,ele):
    for item in list:
        if item == ele:
            return True
    return False
import numpy as np
x = np.random.randint(11,size= 1000000)
print(x)
print(old_search(x,0.1))