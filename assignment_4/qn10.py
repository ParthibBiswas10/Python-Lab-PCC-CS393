'''10. Write a program to find the arithmetic mean, variance and standard deviation of any
values in a list'''

l=list(map(int,input("Enter Values by space: ").split()))
mean=sum(l)/len(l)
sum=0
for i in l:
    sum+=(i-mean)**2
var=sum/len(l)
sa=var**0.5

print(f"Mean: {mean}, Varience: {var}, SD: {sa:.2f} ")