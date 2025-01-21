'''8. Write a program to reverse a list without using another list or in-built function'''

l=list(map(int,input("Enter Values by space: ").split()))
for i in range(len(l)-1,-1,-1):
    print(l[i] , end=" ")