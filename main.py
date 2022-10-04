import numpy as np
import os
def creerGrille(taille) :
        grille=np.zeros((taille,taille))
        return grille

def afficherGrille (grille) :
        clear = lambda: os.system('cls')
        clear()
        print(grille)
        return 0

a=creerGrille(20)
afficherGrille(a)

