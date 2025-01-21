'''2. Write a Python function that accepts a string and calculates the number of uppercase letters
and lowercase letters.'''

n=input("Input a String: ")
up=lp=0
for i in n:
    if(ord(i)) in range(65,91):
        up+=1
    if(ord(i)) in range(97,122):
        lp+=1
print(f"No of Uppercase letters: {up} & Number of LowerCase letter: {lp}")





#2nd Method:
up=lp=0
for i in n:
    if i.isupper():
        up+=1
    if i.islower():
        lp+=1
print(f"using 2nd method:\nNo of Uppercase letters: {up} & Number of LowerCase letter: {lp}")