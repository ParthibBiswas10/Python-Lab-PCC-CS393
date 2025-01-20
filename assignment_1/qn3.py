'''Write a program to take a 2-digit number and then print the reversed number. That is, if
the input given is 25, the program should print 52. Then extend it for 3-digit number and also
check for odd and even'''


n=int(input("Enter Number: "))
rev=int(str(n)[::-1])
print(f"reverse number : {str(n)[::-1]}")
if(n%2==0):
    print("Given Number is Even")
else:
    print("Given Number is odd")

if(rev%2==0):
    print("Reversed Number is Even")
else:
    print("Reversed Number is odd")