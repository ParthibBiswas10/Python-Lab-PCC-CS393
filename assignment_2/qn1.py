'''1. I. A store charges Rs120 per item if you buy less than 10 items. If you buy
between 10 and 99 items, the cost is Rs100 per item. If you buy 100 or more
items, the cost is Rs70 per item. Write a program that asks the user how many
items they are buying and prints the total cost'''

items=int(input("Kota item kinbi? "))
if items<10:
    print(f"Tui dibi {items*120} taka")
elif items>=10 and items<=99:
    print(f"Tui dibi {items*100} taka")
else:
    print(f"Tui dibi {items*70} taka")
    