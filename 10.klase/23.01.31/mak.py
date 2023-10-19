Skaitlis=0
while not (Skaitlis>0):

    Skaitlis=int(input("ievadi veselu pozitīvu skaitli: "))
summa=0

while Skaitlis>0:
    if Skaitlis>9: 
        print(Skaitlis%10, end=" + ")
    else: 
        print(Skaitlis%10, end=" - ")
    summa += Skaitlis%10
    Skaitlis=int(Skaitlis/10)

print(summa)


#nedomāju ir pareizi uzrakstīts