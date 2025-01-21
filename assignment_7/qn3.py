'''3. Write a python program to perform the elements-wise multiplication of two 3X3 Matrices'''

import numpy as np
matrix1=np.random.randint(0,10,(3,3))
matrix2=np.random.randint(0,10,(3,3))
print(matrix1)
print(matrix2)

print(f"mul of Matrices: \n{matrix1*matrix2}")