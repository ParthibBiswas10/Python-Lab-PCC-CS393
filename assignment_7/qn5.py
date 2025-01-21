import numpy as np
matrix1=np.random.randint(0,10,(3,3))

print(matrix1)
rs=matrix1.max(axis=1)
cs=matrix1.max(axis=0)

'''another method:  
rs=np.amax(matrix1,axis=1)
cs=np.amax(matrix1,axis=0)'''


print(f"Max in Row: {rs}")
print(f"Max in column: {cs}")
