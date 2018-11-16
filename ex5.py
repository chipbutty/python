# List overlap
a = [1, 1, 2, 3, 5, 8, 12, 15, 21, 34, 55, 89]
b = [1, 2, 55, 4, 5, 7, 8, 9, 10, 11, 12, 13, 15]
print (a, b)
import numpy as np
c = np.in1d(a,b)
print (c)
d = np.intersect1d(b, a)
print (d)