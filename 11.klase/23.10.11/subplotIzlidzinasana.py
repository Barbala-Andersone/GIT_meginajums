import numpy as np
import matplotlib.pyplot as plt

# plt.subplots returns an array of arrays. We can
# directly assign those to variables directly
fig, ((ax1,ax2)) = plt.subplots(1,2)

# sample data in different magnitudes
x = np.linspace(0.0,100,50)
y1 = np.random.normal(loc=10, scale=2, size=10)
y2 = np.random.normal(loc=20, scale=2, size=10)

# plot in each subplot
ax1.plot(y1)
ax2.plot(y2)

ax1.set_ylim(0,25)
ax2.set_ylim(0,25)

plt.show()