'''8. Write a program that will check if a number is a magic number or not. (A
magic number is that number whose repeated sum of its digits till we get a single
digit is equal to 1. Ex: 1729 1+7+2+9=19 1+9=10 1+0=1)'''

def magic(a):

    if a==10:
        print("Magic Number")
        return
    elif a<10:
        print("Not magic Number")
    else:
        i=0
        sum=0
        while(a>0):
            sum=sum+(a%10)
            a//=10
            i=i+1
        magic(sum)

n=int(input("Enter NUmber: "))
magic(n)