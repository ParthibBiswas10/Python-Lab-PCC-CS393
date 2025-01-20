'''2. Write a short program to check whether the square root of a number is prime or
not.'''

import math
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n = int(input("Enter a number: "))
if n < 0:
    print("Invalid input")
else:
    sq = math.sqrt(n)
    print(f"sqr root: {sq}")
    if sq.is_integer():  
        if is_prime(int(sq)):
            print("The square root is prime.")
        else:
            print("The square root is not prime.")
    else:
        print("The square root is not an integer, so it cant be prime.")
