class Canard:
    def __init__(self,taille,age):
        self.taille = taille
        self.age = age            

    def nager(self):
        print("Je suis un carnard MyLib de {} m et je nage".format(self.taille))

    def sensvoler(self):
        print("Je suis un canard de MyLib et je m'envole")