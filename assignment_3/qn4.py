'''Write a program to check whether a user input string is palindrome or not.'''

n=input("Enter String: ")
rev=n[::-1]
if(n==rev):
    print("Pallindrome")
else:
    print("Not Palli")