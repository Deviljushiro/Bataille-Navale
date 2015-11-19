import Position

class Bateau:

    def __init__(self, listPieces, size):
        self.size = size
        self.listPieces = listPieces
        

    def SuppMorceau(self, p = Position):
        self.listMorceau.remove(p)
        return self
        
    def estTouche(self, tir = Position):
        if (tir in self.listPieces):
            self.size = self.size - 1
            return True
        else:
            return False

    def estCoule(self, tir = Position):
        return (self.size==0)

    def estEnVue(self, tir = Position):
        return ((not(estTouche(tir)))and(tir.x in self.listPieces or tir.y in self.listPieces))

    def estRate(self, tir = Position):
        return ((not(estTouche(tir)))and(not(estEnVue(tir))))
    
