def addition(r1,c1):
    return [[mat1[i][j]+mat2[i][j] for j in range(col1)] for i in range(row1)]

def sub(r1,c1):
    return [[mat1[i][j]-mat2[i][j] for j in range(col1)] for i in range(row1)]

def mul(r1,c1,r2,c2):
    result=[]
    
    for i in range(r1):
        row=[]
        for j in range(c2):
            a=0
            for k in range(c1):
                a=mat1[i][k]*mat2[k][j]+a
                row.append(a)
        result.append(row)
    return result
            

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
        a=int(input(f"enter ({i},{j}): "))
        row.append(a)
    mat1.append(row)

print("Enter Values of MAtrix 2: ")
for i in range(row2):
    row=[]
    for j in range(col2):
        a=int(input(f"enter ({i},{j}): "))
        row.append(a)
    mat2.append(row)

print("Matrix1: ")
for row in mat1:
    print(row)

print("Matrix2: ")
for row in mat2:
    print(row)

print("Addition :")
if row1!=row2:
    print("Adiition Not possible !!")
else:   
    add_result=[]
    add_result=addition(row1,col1)
    for row in add_result:
      print(row)

print("Subtraction :")
if row1!=row2:
    print("Subtraction Not possible !!")
else:   
    sub_result=[]
    sub_result=sub(row1,col1)
    for row in sub_result:
      print(row)

print("Multiplication :")

 
mul_result=[]
mul_result=mul(row1,col1,row2,col2)
for row in mul_result:
    print(row)

