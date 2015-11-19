import Bateau

class Flotte:

    def __init__(self, listBateau = []):
        self.listBateau = listBateau

    def AjoutBateau(self, b=Bateau):
        self.listBateau.append(b)
        return self

    def SuppBateau(self, b=Bateau):
        if (len(b.listPieces)==0):
            self.listBateau.remove(b)
        return self

    def NombreBateau(self):
        return len(self.listBateau)        

    
        
