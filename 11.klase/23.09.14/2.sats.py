def gridas_izmaksas(cena, linoleja_platums, telpas_platums, telpas_garums):

    summa=0

    import math

    telpas_garums=math.ceil(telpas_garums)
    telpas_platums=math.ceil(telpas_platums)

    telpas_lielums=telpas_platums*telpas_garums



    linoleja_rulli=telpas_platums/linoleja_platums
    linoleja_rulli=math.ceil(linoleja_rulli)
    izmaksas=telpas_lielums*cena

    print(f"Izmaksas ir {izmaksas} EUR. Ir jāiepērk {linoleja_rulli} ruļļi linoleja.")

    return summa

gridas_izmaksas(2,3,6.5,9.234)

"""
    input("Ievadīt linoleja ruļļa platumu metros: ")
    input("Ievadīt telpas platumu metros: ")
    input("Ievadīt telpas garumu metros: ")

    telpas_lielums=telpas_garums*telpas_platums
    linelejs=cena*linoleja_platums
    izmaksas=telpas_lielums*linelejs

    print("Cena ir {izmaksas} EUR.")
"""