import math

class Figure:
    def __init__(self):
        pass
    
    def getPerimetre(self):
        return -1
    
    def getSurface(self):
        return -1
    
class Carre(Figure):
    def __init__(self,cote):
        super().__init__()
        self.cote = cote
        
    def getPerimetre(self):
        return self.cote * 4
    
    def getSurface(self):
        return self.cote * self.cote
    
class Rectangle(Figure):
    
    def __init__(self,longueur, largeur):
        super().__init__()    
        self.longueur = longueur
        self.largeur = largeur
        
    def getPerimetre(self):
        return (self.longueur + self.largeur) * 2
    
    def getSurface(self):
        return self.longueur * self.largeur
    
class Cercle(Figure):
    
    def __init__(self,rayon):
        super().__init__()
        self.rayon = rayon
    
    def getPerimetre(self):
        return self.rayon * 2 * math.pi   
    
    def getSurface(self):
        return math.pow(self.rayon,2)
    
class TriangeRectangle(Figure):
    
    def __init__(self, base, hauteur):
        super().__init__()
        self.base = base
        self.hauteur = hauteur
        
    def getHypo(self):
        return math.sqrt(math.pow(self.base,2) + math.pow(self.hauteur,2))    
        
    def getPerimetre(self):
        return self.base + self.hauteur + self.getHypo()
    
    def getSurface(self):
        return self.base * self.hauteur
              
        