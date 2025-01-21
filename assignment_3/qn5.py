'''5. In the Byteland country, a string S is said to super ASCII string if and only if the count of each
character in the string is equal to its ASCII value. In the Byteland country ASCII code of a is 1,
b is 2, …, z is 26. The task is to find out whether the given string is a super ASCII string or not.
If true, then print “Yes” otherwise print “No”.'''

n=input("Enter String: ")
flag=1
for char in n:
    if n.count(char)!=ord(char)-96:
        flag=0
        break
if flag==0:
    print("No")
else:
    print("Yes")
