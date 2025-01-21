l=list(map(int,input("Enter Values by space: ").split()))
new=[]
for i in l:
    if l.count(i)==1:
        new.append(i)
for i in l:
    if l.count(i)>1:
        new.append(i)
print(new)