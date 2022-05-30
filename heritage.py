class Volaile:
    def __init__(self,couleur,poids):
        self.couleur = couleur
        self.poids = poids

    def sensvoler(self):
        print("Je suis une volaile et je m'envole")   

    def atterir(self):
        print("Je suis une volaile et j'atteris")

class Canard(Volaile):
    def __init__(self, couleur, poids,taille,age):
        super().__init__(couleur, poids) 
        self.taille = taille
        self.age = age            

    def nager(self):
        print("Je suis un carnard de {} m et de je nage".format(self.taille))

    def sensvoler(self):
        print("Je suis un canard et je m'envole")

class Poulet(Volaile):
    def __init__(self, couleur, poids):
        super().__init__(couleur, poids)

    def chanter(self):
        print("Je suis un poulet et je chante")         