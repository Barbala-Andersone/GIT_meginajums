#problēma: Grib materiāla veidu un 
#izmēru podestiem atomātiski


def materialuUzskaite(tips, izmers1, izmers2, skaits):
    if tips == "FINIERIS":
        print(f"Uzskaitīt {skaits} gab. finiera plāksnes, izmēri: {izmers1} cm x {izmers2} cm")
        #ievietojiet šeit kodu, lai veiktu finiera plāksnes uzskaiti:
        
        
    elif tips == "LISTE":
        print(f"Uzskaitīt {skaits} gab. listes detaļas, garums: {izmers1} cm")
        #aprēķins līstes detaļu uzskaitei:
        
        
    elif tips == "STURIS":
        print(f"Uzskaitīt {skaits} gab. stūtu, izmēri: {izmers1} cm x {izmers2} cm")
        #stūru uzskaite:
        
        
    else:
        #ja ir neatpazīts materiāls
        print("Nederīgs tips")

    return
def materialuAprekins(garums, platums, augstums, skaits):
    
    if garums <= 0 or platums <= 0 or augstums <=0 or skaits <= 0:
        print("Nederīgi parametri. Visi parametri jābūt pozitīviem skaitļiem un skaitīt jābūt lielākiem kā 1")
        return
    
    if augstums==1:
        tips="FINIERIS"
        izmers1= garums
        izmers2= platums
        
    elif augstums==2:
        tips="LISTE"
        izmers1 = garums
        izmers2 = None
        
    elif augstums==3:
        tips= "STURIS"
        izmers1 = garums
        izmers2 = platums
        
    else:
        print("Nederīgs augstums. Augstumam jābūt 1, 2 vai 3.")
        return



#piemēri, kā izsaukt funkciju:
materialuAprekins(100, 50, 1, 5) # Pieņemsim, ka finiera plāksnes augstums ir 1
#materialuAprekins(80, 30, 2, 10) #P., ka listes augstums ir 2
#materialuAprekins(60, 60, 3, 8) #P., ka stūriem augstums ir 3