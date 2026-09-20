import numpy as np

a = np.array([[1,2,3],
              [4,5,6]])


''' ndim : the number of dimensions of an array is contained in the ndim attribute.'''

print(a.ndim) #2

''' shape : The shape of an array is a tuple of non-negative integers that specify the number of elements along each dimension. '''

print(a.shape) #(2,3)

print(len(a.shape) == a.ndim)   #true

''' size: The fixed, total number of elements in array is contained in the size attribute.'''

print(a.size)  #6

''' dtype : The data type is recorded in the dtype attribute'''

print(a.dtype)