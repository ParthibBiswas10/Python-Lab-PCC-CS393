'''1. Write a python program to create a 3X3 Matrix randomly and calculate the sum of the
diagonal elements.'''

import numpy as np
matrix=np.random.randint(0,10,(3,3))
print(matrix)
dia_sum=np.trace(matrix)
print(f"Sum of Diagonal Elements: {dia_sum}")