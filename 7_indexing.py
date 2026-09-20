import numpy as np

arr = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

''' Slicing is supported '''

print(arr[0:2])

print(arr[1][0:2])

''' Boolean Indexing '''

numb = arr[ arr >= 6]

print(numb)

even = arr[ arr % 2 == 0]

print(even)

''' Fancy Indexing '''

print(arr[0,1,2]) # prints the 0th 1st and 2nd element respectively 

print(arr[[0,1,2],[1,0,2]]) # prints the arr[0][1], arr[1][0], arr[2][2]