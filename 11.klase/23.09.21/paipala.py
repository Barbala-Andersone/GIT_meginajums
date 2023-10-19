class Laiks:
    def __init__(self, stundas=0, minutes=0, sekundes=0):
        self.stundas=stundas
        self.minutes=minutes
        self.sekundes=sekundes

        if(stundas>=0 and stundas<=9):
            #lai aizpildītu priekšu ar 0
            self.stundas=str(stundas).zfill(2)

        if(minutes>=0 and minutes<=9):
            #lai aizpildītu priekšu ar 0
            self.minutes=str(minutes).zfill(2)
        
        if(sekundes>=0 and sekundes<=9):
            #lai aizpildītu priekšu ar 0
            self.sekundes=str(sekundes).zfill(2)

    def uzstadit_laiku(self, stundas, minutes, sekundes):
        self.stundas=stundas
        self.minutes=minutes
        self.sekundes=sekundes

        if(stundas>=0 and stundas<=9):
            #lai aizpildītu priekšu ar 0
            self.stundas=str(stundas).zfill(2)
        if(minutes>=0 and minutes<=9):
            #lai aizpildītu priekšu ar 0
            self.minutes=str(minutes).zfill(2)
                
        if(sekundes>=0 and sekundes<=9):
            #lai aizpildītu priekšu ar 0
            self.sekundes=str(sekundes).zfill(2)


    def izvadi_laiku(self):
        print("Laiks ir", self.stundas, self.minutes, self.sekundes)

 #   def nākamajā stundā
 # pārbaudīt, kā strādā