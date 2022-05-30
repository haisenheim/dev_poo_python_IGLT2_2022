import heritage
import MyLib
import InfoLib

canard1 = heritage.Canard("Bleu",7,0.6,2)
''' canard1.nager()
canard1.sensvoler()
canard1.atterir() '''
''' 
pond1 = heritage.Pondeuse();

print(pond1.getNombre())

print(isinstance(canard1, heritage.Volaile)) '''

class Caneton(InfoLib.Canard,MyLib.Canard):
    def __init__(self, taille, age):
        super().__init__(taille, age)
        
        
        
cnt= Caneton(12,30)

# print(isinstance(cnt, InfoLib.Canard))     

cnt.nager()   


