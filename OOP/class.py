
##Classe principale (personneage de dessin animé)
class perso:
    def __init__(self, nom, origine, creation, type):
        self.nom = nom
        self.origine = origine
        self.creation = creation
        self.type = type




##Sous-classes dépendant de la première
class humain(perso):
    def __init__(self, nom, origine, creation, metier, pouvoirs, couleurcheveux):
        perso.__init__(self, nom, origine, creation, 'humain')
        self.metier = metier
        self.pouvoirs = pouvoirs
        self.couleurcheuveux = couleurcheveux
        
    def PresenteToi (self):
        print ("Je m'appelle " + self.nom)
        
    def Royale (self):
        if (self.metier == 'princesse'):
            print("J'attend mon prince charmant \n Je suis royale")
            return ("oui")
        elif (self.metier in ["roi", "reine","prince"]):
            print ("Je suis royal")
            return ("oui")
        else:
            print("Je suis du bas-peuple")
            return ("non")



class animal(perso):
    def __init__(self, nom, origine, creation, espece, parle):
        perso.__init__(self, nom, origine, creation, 'animal')
        self.espece = espece
        self.parle = parle
        
    def PresenteToi(self):
        if (self.parle == 'oui'):
            print ("Je m'appelle " + self.nom)
        else:
            print ('...')
    
    def Pokemon(self):
        if (self.espece == "pokemon"):
            print (self.nom + " " + self.nom)
       
    



##Main: intéraction entre 2 personnages

def main():
    #Premier personnage de dessin animé: Sacha 
    Sacha = humain("Sacha", "pokemon", "1996", "Dresseur de pokemon", "non", "noir")
    
    #Deuxieme personnage: carapuce 
    Carapuce = animal("Carapuce", "pokemon", "1996", "pokemon", "non")
    
    #Discussion entre les 2 personnages
    humain.PresenteToi(Sacha)
    animal.PresenteToi(Carapuce)
    
    humain.Royale(Sacha)
    animal.Pokemon(Carapuce)
    

