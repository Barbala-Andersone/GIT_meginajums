import matplotlib.pyplot as plt
import numpy as np

# sample data
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)

# create figure and axes
fig, (ax1,ax2) = plt.subplots(1,2) # 1 row, 2 columns

# just plot things on each individual axes
#ax1.scatter(x,y,c='red',marker='+')
ax2.bar(x,y)

plt.show()