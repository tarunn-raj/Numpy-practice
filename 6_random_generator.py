import numpy as np

rng = np.random.default_rng(10)  # here it returns a genrator object where the seed value is set as 10

''' rng.random()'''

print( rng.random())  # It prints the random float between [0, 1)

''' rng.integers(1,10,8)'''

print(rng.integers(1,10))   ## any one integer in [1,10)

print(rng.integers(1,10,10))  ## 10 randome integers in [1,10)

''' rng.uiform() '''

rng.uniform(1, 2, 4)   # 4 floats in [1, 2)


##  rng.normal()



