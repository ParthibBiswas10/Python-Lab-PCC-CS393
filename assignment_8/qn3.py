'''3. Generate 30 random 2-d points and draw it using a scatter plot'''

import numpy as np
import matplotlib.pyplot as plt 
x=np.random.randint(1,100,(30))
y=np.random.randint(1,100,(30))
s=np.random.randint(30,86,(30))
c = np.random.rand(30, 3)
plt.scatter(x,y,sizes=s,c=c,marker="+")
plt.show()