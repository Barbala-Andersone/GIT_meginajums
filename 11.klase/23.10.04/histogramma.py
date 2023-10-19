# Histogrammas izveide (stabiņveida diagramma)

import matplotlib.pyplot as plt
import numpy as np

# Ģenerēju gadījuma datus
data = np.random.randn(1000)

# Izveidoju histogrammu
plt.hist(data,bins=20,edgecolor="k")

# Pievienoju nosaukumu un apzīmējumus
plt.title("Histogramma")
plt.xlabel("Vērtība")
plt.ylabel("Biežums")

#Parādām histogrammu 
plt.show()