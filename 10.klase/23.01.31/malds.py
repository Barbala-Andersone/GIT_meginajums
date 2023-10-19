#cikls, kas sākas ar 1, beidzas ar 8, kuru neieskaita
sk=1
summa=0
for i in range(1,8):
    summa=summa+sk
    sk=sk*2

print(summa)

"""
i     sk     summa
1     1       1
2     2       1+2
3     4       4+4
4     8       15

"""
#Sastādīt programmu, kas nosaka, vai lietotāja
# ievadītais trīsciparu skaitlis ir simetrisks, t.i.
# skaitļa pirmais un pēdējais cipars ir vienādi.
""" 101, 292, 353, 414..."""
#Programmā iekļaut ievaddati pārbaudi:
# ja lietotājs ievada skaitli, kas nav trīsciparu,
# programma paziņo par kļūdu un prasa ievadīt citu skaitli.
"""
skaitlis=0

while not(skaitlis>99 and skaitlis<1000):
    skaitlis=int(input("Ievadi 3-ciparu skaitli: "))

simti=int(skaitlis//100)
vieni=skaitlis%10 # 127%10=7

print(skaitlis, end="")

if simti==vieni:
    print(end=" ir ")
else:
    print(end=" nav ")
print("simatrisks")

"""

# Sastādīt programmu, kas aprēķina lietotāja ievadītā 
# veselā skaitļa ciparu summu.
skaitlis=0

while not (skaitlis>0):
    skaitlis=int(input("Ievadi veselu pozitīvu skaitli: "))

tukst=int(skaitlis//1000)
simti=int(skaitlis%1000//100)
# var arī :
"""
simti=int(skaitlis//100)
desmiti=(int(skaitlis)-int(simti)*100)//10
"""
desmiti=int(skaitlis%100//10)
vieni=skaitlis%10 #234/10=24.4, bet 234%10=4

summa=tukst+simti+desmiti+vieni
print(summa)

