import numpy as np
""" 


# np.zeros()

a = np.zeros(2)
print(a)

'''While the default data type is floating point (np.float64), you can explicitly specify which data type you want using the dtype keyword'''

a = np.zeros(2,dtype = np.int64)    #first argument is equivalent to (2,)

print(a)

## creating two or more dimensional array

a = np.zeros((2,2),dtype = np.int64)  # first argument is shape

print(a) """

''' ******************************************************************'''

'''   np.ones()  '''

a = np.ones(1)
print(a)

a = np.ones(1,dtype = np.int64)
print(a)

a = np.ones((3,2),dtype = np.int64)
print(a)


'''************************************************************************'''

''' np.empty()  : The function empty creates an array whose initial content is random and depends on the state of the memory. The reason to use empty over zeros 
(or something similar) is speed - just make sure to fill every element afterwards! '''

a = np.empty((4,4))
print(a)

''' np.arange()'''

a = np.arange(4)
print(a)

'''  an array that contains a range of evenly spaced intervals. To do this, you will specify the first number, last number (its excluded), and the step size.'''

a = np.arange(2,10,2)

print(a)

''' np.linspace()  : You can also use np.linspace() to create an array with values that are spaced linearly in a specified interval:'''

a = np.linspace(0,10,num=5)
print(a)