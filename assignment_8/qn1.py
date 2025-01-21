''' Generate randomly monthly electricity bill of a year then plot the bill using a line, bar and
pie char'''

import numpy as np
import matplotlib.pyplot as plt
month=["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
bill=np.random.randint(1000,2000,(12))
plt.xlabel("Month")
plt.ylabel("Electricity Bill")
print("1. line graph, 2.Bar graph, 3.Pie chart")
choice=int(input("Enter Choice: "))
if(choice==1):
    plt.title("Line Graph: ",fontsize=15)
    plt.plot(month,bill,linewidth=1.2)
if(choice==2):
    plt.title("Bar Graph: ",fontsize=15)
    plt.bar(month,bill,edgecolor="r",linewidth=1.2)
if(choice==3):
    plt.title("Pie Chart: ",fontsize=15)
    plt.pie(bill,labels=month,radius=0.9,wedgeprops={'edgecolor':'black'},  textprops={'fontsize': 7} ,autopct="%1.2f%%")

plt.show()

