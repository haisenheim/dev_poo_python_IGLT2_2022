import Lib

c4 = Lib.Carre(4)
rt38 = Lib.Rectangle(8,3)
cr4 = Lib.Cercle(4)
cr1_5 = Lib.Cercle(1.5)
tr86 = Lib.TriangeRectangle(6,8)
c10 = Lib.Carre(10)

sg = c4.getSurface() + rt38.getSurface() + cr4.getSurface()/4 + cr1_5.getSurface()/2 + tr86.getSurface() + c10.getSurface()

print("La surface globale est : {} m2".format(sg))
 
