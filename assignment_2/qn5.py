''' Write a program to print a inverted full pyramid of *.'''

n=int(input("Enter Number of lines:"))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*i+"*"*(i-1))
