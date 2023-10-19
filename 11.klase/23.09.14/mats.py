def pasuti_tkreklus(skaits, apdruka, piegade):
    #Definējam cenas, atbilstoši apdrukas veidam
    cena=0

    if apdruka=="TEKSTS":
        cena=5
    elif apdruka=="ZIME":
        cena=7
    elif apdruka=="FOTO":
        cena=20
    #aprēķināt pasūtījuma cenu
    pasutijuma_cena= skaits*cena

    #pārbauda piegādes nosacījumus
    if pasutijuma_cena <50:
        piegade+=15
    if pasutijuma_cena>100:
        atlaide=pasutijuma_cena*0.05
        pasutijuma_cena= pasutijuma_cena-atlaide
    return pasutijuma_cena   

#testa piemēri

cena=pasuti_tkreklus(10,"TEKSTS",True)
izvads="Kreklu cena ir {} EUR."
print(izvads.format(cena))

cena=pasuti_tkreklus(20,"ZIME",False)

print(izvads.format(cena))