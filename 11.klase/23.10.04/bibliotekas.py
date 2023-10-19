# matplotlib ir jāinstalē ar...(terminālā) pip install matplotlib
import matplotlib.pyplot as plt
# populāra  ārēja bibliotēka datu vizualizācijai

# Vienkāršu līniju grafika izveide
x=[1,2,3,4,5]
y=[10,12,5,8,15]

#svarīgākais, ka abu skaitļu sarakstiem ir vienāda skaita 

#  Izveidojam līniju grafiku
# darbina biblioteku 
plt.plot(x,y)

# pievienojam nosaukumus un apzīmējumus
plt.xlabel("X ass")
plt.ylabel("Y ass")
plt.title("Vienkāršu līniju grafiks")

# Parādām grafiku
plt.show()