import Position
import Bateau

class Grille:

        def __init__(self, grille = list()):
            self.grille = grille


        
            
        

        def CoordAppartient(self, p=Position):
            return(p in self)

        def CoordValide(self, p=Position):
            return not((p.x>20 or p.x<0) or (p.y>20 or p.y<0) or self.CoordAppartient(self,p)) 
              
         

        
