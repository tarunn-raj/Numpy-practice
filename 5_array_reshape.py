import numpy as np

''' arr.reshape() : Using arr.reshape() will return a reshaped array without changing the data. Just remember that when you use the reshape 
method, the array you want to produce needs to have the same number of elements as the original array. If you start with an array with 12 
elements, youll need to make sure that your new array also has a total of 12 elements '''

a = np.arange(6)
print(a)

b = a.reshape(3,2)
print(b)

c = a.reshape(1,2,3)
print(c)


''' With np.reshape, you can specify a few optional parameters:'''

print(np.reshape(a, shape=(1, 6), order='C'))

'''`order='C'` in NumPy:

- `'C'` means C-style (row-major) order.
- When reshaping, NumPy reads the elements row by row.
- It does not change the values; it only changes how they are arranged.

Example:

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

np.reshape(a, (3, 2), order='C')

Output:
[[1 2]
 [3 4]
 [5 6]]

The elements are read as:
1 → 2 → 3 → 4 → 5 → 6

Remember:
order='C' → read elements row by row (row-major order).

`order='C'` is also the default order of np.reshape(), so:

np.reshape(a, (3, 2))

and

np.reshape(a, (3, 2), order='C')

are equivalent. '''