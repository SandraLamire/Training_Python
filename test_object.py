class PartyAnimal:
    # si on veut que chaque instance ait sa propre valeur de x : 
    # déclarer x comme un attribut d'instance
    # def __init__(self):
    #     self.x = 0
    
    # Sinon, ici x est un attribut de classe (plutôt qu'un attribut d'instance)
    # Cela signifie que x est partagé entre toutes les instances de la classe PartyAnimal. 
    # Lorsqu'une instance modifie la valeur de x, cette modification est partagée entre toutes les instances.
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print("So far",self.x)

        
an = PartyAnimal()

# = Partyanimal.party(an)
an.party()			
# So far 1
an.party()
# So far 2
an.party()
# So far 3


class PartyAnimal2:
    x = 0
    def __init__(self, nam):
        self.name = nam
        print(self.name, "constructed")
        
    def party2(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)
        
# appel au constructeur __init__ à la création d'une instance       
q = PartyAnimal2("Quincy")
# Quincy constructed
m = PartyAnimal2("Mia")
# Mia constructed

# lancement du code party2 à l'appel de la méthode de classe
q.party2()
# Quincy party count 1
m.party2()
# Mia party count 1
q.party2()
# Quincy party count 2

class FootballFan(PartyAnimal2):
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party2()
        print(self.name, "- points :", self.points)

s = PartyAnimal2("Sally")
# Sally constructed
s.party2()
# Sally party count 1

j = FootballFan("Jim")
# Jim constructed
j.party2()
# Jim party count 1
j.touchdown()
# Jim party count 2 (car self.party2() appelé à nouveau dans FootballFan)
# 7

