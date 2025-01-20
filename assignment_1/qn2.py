'''2. Write a program to calculate the amount payable after simple and compound interest.
Simple Interest = (P ⋆ t ⋆ r) / 100
Compound Interest = P ⋆ ((1 + r / 100)^t - 1)'''

p=int(input("Enter Principal Value: "))
t=int(input("Enter Time in Years: "))
r=int(input("Enter rate: "))

si=(p*r*t)/100
ci=round(p*((1+(r/100))**t -1),3)

print(f"Amonut payable after Simple Interest: {si+p}")
print(f"Amonut payable after compound Interest: {ci+p:.3f}")


