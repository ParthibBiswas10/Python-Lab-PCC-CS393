'''3. Write a Python function to check whether a string is a pangram or not.
Note : Pangrams are words or sentences containing every letter of the alphabet at least
once.
For example : “The quick brown fox jumps over the lazy dog”.'''

n=input("Enter String: ")
new=n.lower()
new=new.replace(" ","")
#print(new)
l=[]
flag=0
for i in new:
    l.append(ord(i))

for j in range(97,123):
    if j not in l:
        flag=0
    else:
        flag=1
if flag==0:
    print("Not palgram")
else:
    print("Palgram")