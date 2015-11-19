from Flotte import Flotte
from Bateau import Bateau
from Position import Position

class Joueur:

    def __init__(self, actif=False, flotte = Flotte):
        self.actif = actif
        self.flotte = flotte


    def PlacerBateau(self, b= Bateau):
            print("You have a size ship! Where do you want to place it? (coordinates and direction) \n")
            print("x= \n")
            x = int(input(int))
            print("y= \n")
            y = int(input(int))
            print("direction = (0 = Hor, 1 = Vert)\n")
            direction = int(input(int))
            nbreBloc = b.size
            if (direction==0):
                while (nbreBloc != 0):
                    p= Position(x,y)
                    b.listPieces.append(p)
                    y = y + 1
                    nbreBloc = nbreBloc - 1
            else:
                while (nbreBloc != 0):
                    p= Position(x,y)
                    b.listPieces.append(p)
                    x = x + 1
                    nbreBloc = nbreBloc - 1
            self.flotte.AjoutBateau(b)
            return self

    def NbreBateauxRestants(self):
            return (5 - len(self.flotte.listBateau))
