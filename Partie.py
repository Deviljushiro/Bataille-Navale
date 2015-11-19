import Joueur

class Partie:

    def __init__(self, joueur1=Joueur, joueur2=Joueur):
        self.joueur1 = joueur1
        self.joueur2 = joueur2

    def creerPartie(self):
        self.joueur1.actif = True

    def JoueurActif(self):
        if (joueur1.actif):
            return joueur1
        else:
            return joueur2

    def JoueurInactif(self):
        if not(joueur1.actif):
            return joueur1
        else:
            return joueur2

    def JoueurSuivant(self):
        self.JoueurActif.actif = False
        self.JoueurInactif.actif = True

    def PartieFinie(self):
        if (joueur1.flotte.NombreBateau==0):
            return ("Le joueur 2 a gagne !")
        elif (joueur2.flotte.NombreBateau==0):
            return ("Le joueur 1 a gagne !")
        
