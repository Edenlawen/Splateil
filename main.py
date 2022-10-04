from array import array
from this import d
import numpy as np
import os


def creerGrille(taille) :
    grille=np.ones((taille,taille))
    return grille

def afficherGrille (grille) :
    clear = lambda: os.system('cls')
    clear()
    print(grille)
    return 0

def creerPion1(grille) :
    grille[10][10]=9
    pion=np.zeros(2)
    pion[0]=10
    pion[1]=10
    return grille, pion


def movePown1(grid,pos):
    step=str(input("Où voulez vous aller ?\n"))
    x=int(pos[0])
    y=int(pos[1])
    if (step == "d") and (y!=len(grid)) :
        grid[x][y+1]=9
        grid[x][y]=4
    elif (step == "q") and (x!=0) :
        grid[x][y-1]=9
        grid[x][y]=4
    elif (step == "s") and (y!=0) :
        grid[x+1][y]=9
        grid[x][y]=4
    elif (step == "z") and (y!=len(grid)) :
        grid[x-1][y]=9
        grid[x][y]=4
    else :
        print("Impossible de se déplacer ici\n Recommencez\n")
        movePown1(grid,pos)
    return grid
        
          
    


a=creerGrille(20)
a,zz=creerPion1(a)
afficherGrille(a)
movePown1(a,zz)
afficherGrille(a)


