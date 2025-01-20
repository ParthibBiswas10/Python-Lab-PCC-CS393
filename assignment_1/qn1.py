'''1. Write a program that asks the number of years as input, and then prints out the number of
days, hours, minutes, and seconds in that number of years. Assume 365 days per year and also
check that year for leap year or not.'''

year=int(input("Enter number of years: "))
leap=year//4
days=365*year+leap
hours=days*24
minutes=hours*60
second=minutes*60
print(f"Number of leap Years: {leap}")
print(f"For {year} years : {days} Days, {hours} Hours, {minutes} Minutes, {second} Seconds")