'''4. Write a program to read two lists num and denum which contain the numerators
and denominators of the same fractions at the respective indexes. Then display the
smallest and largest fraction along with its index.'''

denom=[]
num=[]
size=int(input("koto gulo fraction chai? "))
for i in range(size):
    n=int(input(f"Enter numerator of fraction{i+1}: "))
    num.append(n)
    d=int(input(f"Enter denominator of fraction{i+1}: "))
    denom.append(d)

result=[num[i]/denom[i] for i in range(size)]
max=result[0]
min=result[0]
ma=0
mi=0
for i in range(size):
    if result[i]>max:
        max=result[i]
        ma=i
    if result[i]<min:
        min=result[i]
        mi=i

print(f"maxix Fraction is: {num[ma]}/{denom[ma]} and index: {ma}")
print(f"Min Fraction is: {num[mi]}/{denom[mi]} and index: {mi}")



