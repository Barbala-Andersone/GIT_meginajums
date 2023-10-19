#klases meiteņu un zēnu skaits klasē
import matplotlib.pyplot as plt

"""
skaits=[12,15]
kategorijas= ["Meitenes","Zēni"]

plt.figure(figsize=(8,6))
plt.bar(kategorijas, skaits, color=["pink", "lightBlue"])


plt.title("Zēnu un meiteņu skaits klasē")
plt.xlabel("Kategorija")
plt.ylabel("skaits")

plt.show()
"""


skaits=[12,15]
kategorijas=["Meitenes","Zēni"]
plt.figure(figsize=(8,6))
plt.plot(kategorijas, skaits, marker="o", linestyle="dotted", color="pink", markersize=10)

plt.title("skaits")
plt.xlabel("kategorijas")
plt.ylabel("skaits")

plt.show()
