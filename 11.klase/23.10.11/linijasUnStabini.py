import matplotlib.pyplot as plt

# līnijas

x=[1,-2,3,4,-5]
y=[10,-12,5,-4,15]

plt.plot(x,y)


plt.show()


# stabiņi

skaits=[12,15]
kategorijas= ["Meitenes","Zēni"]

plt.figure(figsize=(8,6))
plt.bar(kategorijas, skaits, color=["pink", "lightBlue"])



plt.show()

