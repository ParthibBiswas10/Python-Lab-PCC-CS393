'''Write a program to input N numbers and then print the second largest number'''
num=[]
n = int(input("Enter the number of elements: "))
for i in range(n):
    a=int(input(f"Enter the number {i+1}: "))
    num.append(a)
num.sort(reverse=True)
#num.reverse()
print("Second largest number is: ",num[1])
