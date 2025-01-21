'''8. Write a program to reverse a list without using another list or in-built function'''

l=list(map(int,input("Enter Values by space: ").split()))
i=0
j=len(l)-1
def swap(l,i,j):
    temp=l[i]
    l[i]=l[j]
    l[j]=temp
while(i<j):
    swap(l,i,j)
    i+=1
    j-=1
print(l)