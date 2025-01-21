import numpy as np
matrix1=np.random.randint(0,10,(3,3))
matrix2=np.random.randint(0,10,(3,3))
print(matrix1)
print(matrix2)
M_sum=np.add(matrix1,matrix2)
print(f"Sum of Matrices: \n{M_sum}")