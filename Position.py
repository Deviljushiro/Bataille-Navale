import Bateau

class Position:

    def __init__(self, x=int, y=int):
        self.x = x
        self.y = y



    def getX(self):
        return self.x
    
    def getY(self):
        return self.y


    def setX(self, x):
        return self.x

    def setY(self, y):
        return self.y

    def getPos(self):
        return (self.x,self.y)

    #def creerPos(x: int, y:int, marque: bool):
 #       return new Position(x,y,marque)
