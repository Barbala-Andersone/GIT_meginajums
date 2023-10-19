#Sastādi programmu, kas lietotājam prasa ievadīt
#divciparu skaitli un aprēķina tā ciparu summu.

#27 .....2+7=9   56.....5+6=11

skaitlis=input("Ievadi divciparu skaitli: ") #ir tags str
sk=len(skaitlis)
if sk==2:
    skaitlis=int(skaitlis) #pārvērtu par int
    desmiti=int(skaitlis/10)
    vieni=skaitlis%10
    print(f"{desmiti+vieni}")
else:
    print("Tas nav divciparu skaitlis!")