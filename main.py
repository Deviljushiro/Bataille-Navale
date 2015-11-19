from Partie import Partie
from Flotte import Flotte
from Bateau import Bateau
from Position import Position
from Joueur import Joueur
from Resultat import Resultat

b = Bateau([],3)
f1= Flotte([])
j1= Joueur(True, f1)
j1.PlacerBateau(b)
for i in range(0,b.size):
    print(b.listPieces[i].getPos())

