"""

1.specifikācija:

def aprekins(a,c):
    s=a*c
    print("Summa ir ", s)
    
aprekins(4,5)

"""
"""

2.specifikācija:

def ievarijums(aboli_svars, cukurs_cena, cukurs_uz_kg):
    izmaksa_kg = cukurs_cena*cukurs_uz_kg
    izmaksas = izmaksa_kg*aboli_svars
    print("Izmaksas būs", izmaksas ,"$")

ievarijums(2,7,0.3)

"""


def izmaksas_receptei(recepte, cena):
    # Funkcija aprēķina izmaksas dotai receptei
    # summējot visu sastāvdaļu izmaksas

    summa = 0
                                                                                                                                            
    for sastavdala in recepte:
        daudzums = recepte[sastavdala]
        summa += daudzums * cena[sastavdala]
    return summa
                                                                                                                                                                             
def izmaksas_kopa(abolu_svars, recepte, cenas):
    izmaksas_kg = izmaksas_receptei(recepte, cenas) / recepte["aboli"]

    ievarijuma_izmaksas = abolu_svars * izmaksas_kg

    print("Uz {} kg ābolu izmaksas būs {:2f} EUR".format(abolu_svars, ievarijuma_izmaksas))

recepte1 = {"cukurs": 0.6, "kanelis": 0.08, "aboli": 3.0, "udens": 0.2}
cenas1 = {"cukurs": 0.9, "kanelis": 33.0, "aboli": 0.0, "udens": 0.0}

izmaksas_kopa(15.0, recepte1, cenas1)