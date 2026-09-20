import numpy as np

''' Sorting of Array'''

""" arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

print(np.sort(arr))  ## sorts the array and return array and doesnt modify the original array

print(arr) """


''' numpy.sort(a, axis=-1, kind=None, order=None, *, stable=None, descending=<no value>)'''

arr = np.array([[2, 28, 5, 3, 7, 4, 6, 8],
               [9,10,11,12,13,14,15,16]])

print(np.sort(arr,-2)) # sort along the second last axis (which is along the rows in this case)
print(np.sort(arr,-1)) # sort along the last axis (which is along column in this case) 


''' Concatenate array :  numpy.concatenate(arrays, /, axis=0, out=None, *, dtype=None, casting='same_kind')'''

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(np.concatenate((a,b)))    # all of the input arrays must have the same shape, except in the dimension corresponding to axis (the first, by default).


x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

print(np.concatenate((x,y)))

''' axis : int, optional
The axis along which the arrays will be joined. If axis is None, arrays are flattened before use. Default is 0.'''




