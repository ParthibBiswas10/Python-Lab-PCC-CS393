import numpy as np
row1=int(input("Row of MAtrix 1: "))
col1=int(input("col of MAtrix 1: "))
row2=int(input("Row of MAtrix 2: "))
col2=int(input("col of MAtrix 2: "))


mat1=[]
mat2=[]
print("Enter Values of MAtrix 1: ")
for i in range(row1):
    row=[]
    for j in range(col1):
        real=int(input(f"enter real of ({i},{j}): "))
        img=int(input(f"enter img of ({i},{j}): "))
        a=complex(real,img)
        row.append(a)
    mat1.append(row)


print("Matrix2: ")
for i in range(row2):
    row=[]
    for j in range(col2):
        real=int(input(f"enter real of ({i},{j}): "))
        img=int(input(f"enter img of ({i},{j}): "))
        a=complex(real,img)
        row.append(a)
    mat2.append(row)
        
mat2=np.array(mat2)
mat1=np.array(mat1)
if mat1.shape==mat2.shape:
    addition=np.add(mat1,mat2)
    subtraction=np.subtract(mat1,mat2)
    print("Additon: ")
    print(addition)
    print("Sub: ")
    print(subtraction)

else:
    print("Order Not Same !!")
if row1==col2:
    multi=np.matmul(mat1,mat2)
else:
    print("Multiplication not Posssible")


print("multiplication: ")
print(multi)

