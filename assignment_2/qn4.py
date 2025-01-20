'''4. Write a program that takes the input until q and print the palindrome numbers'''
number=[]
palli=[]
while True:
    n=input("enter number: ")
    if n=='q' or n=='Q':
        break
    else:
        number.append(n)
        if n==n[::-1]:
            palli.append(n)

print(f"Numbers: {number}")
print(f"Pallindrome Number: {palli}")
    
