'''2. Write a program that takes any two lists L and M of the same size and adds their
elements together to form a new list N whose elements are sums of the corresponding
elements in L and M. For instance, if L = [3, 1, 4] and M = [1, 5, 9], then N should equal
[4,6,13].'''

n=int(input("Enter Size: "))
l=[]
m=[]
for i in range(n):
    a=int(input("Enter Value for 1st List: "))
    l.append(a)
    b=int(input("Enter Value for 2nd List: "))
    m.append(b)
new=[]
for i in range(n):
    a=l[i]+m[i]
    new.append(a)

print(f"Sum of 2 lists: {new}")