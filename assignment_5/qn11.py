'''Write a program that accepts a different number of arguments and returns the sum of only
the positive values passed to it.'''

n=list(map(int,input("Enter numbers: ").split()))
pos=[i for i in n if i>0]
print(f"Sum of positive number: {sum(pos)}")