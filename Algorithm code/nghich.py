from merge_sort import mergeSort
from selection_sort import selection_sort
import numpy as np 
import time
a  = (np.random.rand(1,100000)).ravel()
start_time = time.time()
mergeSort(list(a))
print("--- %s seconds ---" % (time.time() - start_time))
print('---------comparing------------')
start_time = time.time()
selection_sort(list(a))
print("--- %s seconds ---" % (time.time() - start_time))