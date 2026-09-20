import numpy as np


''' np.sum(array,axis ='')'''

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(np.sum(arr,axis = 0))  # will add (1+5+9) (2+6+10) .................

print(np.sum(arr,axis = 1)) # will add (1+2+3+4) (5+6+7+8) .......................



''' np.prod()'''

prod_col = np.prod(arr, axis = 0)

print(prod_col)




''' Operations on two array'''

# Sum of two arrays

a1 = np.array([1,2,3,4])
a2 = np.array([5,6,7,8])
print(a1 + a2)


# Product of two arrays

print( a1 * a2)


# Division of two arrays 

print(a1/a2)

# Modulo Division of two arrays

print(a1 % a2)

