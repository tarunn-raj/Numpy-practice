

import numpy as np

""" print(np.__version__)  ## prints the installed version of numpy

a = np.array([[1,2,3],
              [4,5,6]])

# print(a.shape)

# print(a)
# print(a[0][0])

# a[0] =10

# print(a) """


#*********************************************

''' Also like the original list, Python slice notation can be used for indexing.'''

a = np.array([1,2,3,4,5,6,7,8])


''' One major difference is that slice indexing of a list copies the elements into a new list, but slicing an array returns a view: an object that 
refers to the data in the original array. The original array can be mutated using the view. '''
b = a[:4] 


print(a)
print(b)

b[0] =100

print(a)
print(b)



'''
It is familiar practice in mathematics to refer to elements of a matrix by the row index first and the column index second. This happens to 
be true for two-dimensional arrays, but a better mental model is to think of the column index as coming last and the row index as second to 
last. This generalizes to arrays with any number of dimensions

'''

''' ********************************************************************************'''

'''   DIMENSIONS AND AXIS OF AN ARRAY'''

''''NUMPY: DIMENSIONS, AXES & PHYSICAL SPACE

1. PHYSICAL SPACE DIMENSION

A dimension tells us how many independent coordinates are needed
to locate a point.

1D → one coordinate
     (x)

2D → two coordinates
     (x, y)

3D → three coordinates
     (x, y, z)

Example:
A point (3, 5) exists in 2D physical space because we need
x and y to locate it.

--------------------------------------------------

2. ARRAY DIMENSION

In NumPy, dimension means how many indices are needed to reach
one element of an array.

1D:
a = np.array([10, 20, 30])

a[0]
→ 1 index → 1D → 1 axis

2D:
a = np.array([[1, 2, 3],
              [4, 5, 6]])

a[0, 1]
→ 2 indices → 2D → 2 axes

3D:
a[i, j, k]
→ 3 indices → 3D → 3 axes

--------------------------------------------------

3. AXIS

An axis is a direction along which an array is organized/indexed.

For a 2D array:

       axis 1 →
      0  1  2
axis 0
  ↓   1  2  3
      4  5  6

axis 0 → rows  (first axis)
axis 1 → columns (second axis)

--------------------------------------------------

4. ndim

ndim tells us how many axes an array has.

a.ndim

Example:
a = np.array([[1, 2, 3],
              [4, 5, 6]])

a.ndim → 2

--------------------------------------------------

5. shape

shape tells us how many elements exist along each axis.

a.shape

For the above array:

a.shape → (2, 3)

→ 2 elements along axis 0 (rows)
→ 3 elements along axis 1 (columns)

--------------------------------------------------

6. IMPORTANT: ARRAY DIMENSION ≠ PHYSICAL/DATA DIMENSION

An array can store data representing objects in a higher-dimensional
space without having the same number of axes.

Example:

a = np.array([[2, 7, 1, 9],
              [5, 3, 8, 4],
              [6, 1, 2, 7]])

Array:
→ 2 axes
→ shape = (3, 4)
→ 3 points
→ each point has 4 coordinates

Each point:
(2, 7, 1, 9)

can represent a point in 4D space.

So:

Array → 2 axes
Data represented → points in 4D space

--------------------------------------------------

REMEMBER:

Physical dimension
→ How many coordinates are needed to describe a point?

Array dimension / ndim
→ How many axes does the NumPy array have?

Axis
→ One indexing direction of an array.

shape
→ How many elements are present along each axis?

index
→ Used to select a particular element.'''


''' ************************************************************************'''

'''Another difference between an array and a list of lists is that an element of the array can be accessed by specifying the index along 
each axis within a single set of square brackets, separated by commas.'''

a = np.array([[1,2,3],
              [4,5,6]])

print(a[0,2])  # 3