

class perso:
  def __init__(self,nom,origine,creation,type):
    self.nom=nom
    self.origine=origine
    self.type=type
    
    
 class humain(perso):
  def __init__(self,nom,origine,creation,metier,pouvoir,couleurcheveux):
    perso.__init__(self,nom,origine,creation,"humain")
    self.pouvoir=pouvoir
    self.couleurcheveux=couleurcheveux
  def PresenteToi(self):
     print("Je m' appelle " ,self.nom)
  def Royal(self):
      if(self.metier == 'princesse'):
          print("J'atend mon prince charmant")
          return("oui")
        elif
    
    
class animal(perso):
  def __init__(self,nom,origine,creation,espece,parle):
    perso.__init__(self,nom,origine,creation,"animal")
    self.espece=espece
    self.parle=parle
  def presenteToi(self):
    if(self.parle=="oui"):
      print('Je m'appelle', self.nom)
     else:
     print("...")
      
    
