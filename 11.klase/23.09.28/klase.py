# funkcija ir programmas strukturēšanas līdzeklis
#snake metode m_m

"""
#Ja funkcijai nav parametri:


def bul_stul():
    return print("Labrīt!")

bul_stul()
"""

"""
def bul_stul(a,b):
    return a*b

#aste=bul_stul(2,5)
#print(aste)
#vai
#print(bul_stul(2,5))
"""



"""
# lambda funkcija
summa=lambda a,b: a*a+b
print(summa(5,7)) #izsauc lambda funkciju

# funkcijas alternatīvs
def mana_summa(n):
    return lambda a: a+n

#print(mana_summa(7)) # atgriež lambda funkciju (nedarbojas)
#print(mana_summa(7)(5)) # atgriezīs rezultātu (darbojas)

#mana_summa2=mana_summa(7) # 7 ieliek n vietā
#print(mana_summa2(5)) # 5 ieliek a vietā
"""

"""                                                                            
# Lambda funkcija, kas izmanto sarakstu filtrēšanu
skaitlis=[1,2,3,4,5,6,7,8,9,10]
para_skaitli=list(filter(lambda x: x%2==0 or x%3==0, skaitlis))
print(para_skaitli)
"""

"""
# Lambda funkcija, kas izmanto sarakstu pārveidošanu (map)
skaitlis=[1,2,3,4,5]
skaitlis_kvadrata=list(map(lambda x: x**2, skaitlis))
print(skaitlis_kvadrata)
"""

                                                                                                          
"""
# Lambda funkcija, kas izmanto kārtošanu
cilveki=[{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]
cilveki.sort(key=lambda persona: persona["age"])
print(cilveki)
"""

"""
paka=lambda x, n=2: x**n
rez1=paka(3) # izmanto argumenta noklusējuma vērtību
rez2=paka(2,5) # aizvieto argumante noklusējuma vērtību
print(rez2)
"""

class Celojums:
    def __init__(self, vieta, datums, izmaksas):
        self.vieta=vieta
        self.datums=datums
        self.izmaksas=izmaksas

    def informacija(self):
        print(f"Ceļojums uz {self.vieta}")
        print(f"Datu: {self.datums}")
        print(f"Izmaksas: {self.izmaksas} EUR")



class Celotajs:
    def __init__(self, vards, uzvards, pieredze):

        self.vards = vards
        self.uzvards = uzvards
        self.pieredze = pieredze

        self.celojumi = []


    def pievienot_celojumu(self, celojums):
        self.celojumi.append(celojums)
    
    def informacija(self):
        print(f"Celotājs: {self.vards} {self.uzvards}")
        print(f"Pieredze: {self.pieredze} gadi")
        print("Veiktie ceļojumi:")

        for celojums in self.celojumi:
            print("-----")
            celojums.informacija()

# Objektu izveidošana

celojums1 = Celojums("Parīze, Francija", "2023-05-15", 1000)
celojums2 = Celojums("Roma, Itālija", "2023-07-10", 1200)

celotajs1 = Celotajs("Anna", "Pavlova", 5)
celotajs2 = Celotajs("Juris", "Ozols", 10)

# Ceļojumu pievienošana ceļotājiem

celotajs1.pievienot_celojumu(celojums1)
celotajs2.pievienot_celojumu(celojums1)
celotajs2.pievienot_celojumu(celojums2)

# Objektu izmantošana

celotajs1.informacija()
print("\n")
celotajs2.informacija()

