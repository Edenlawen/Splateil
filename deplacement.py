from array import array
from this import d
import numpy as np
import os
import bonus


def creerGrille(taille) :
    grille=np.ones((taille,taille))
    return grille

def afficherGrille (grille) :
    clear = lambda: os.system('cls')
    clear()
    print(grille)
    return 0

def creerPion1(grille) :
    grille[5][5]=9
    pion=np.zeros(2)
    pion[0]=5
    pion[1]=5
    return grille, pion

def creerPion2(grille) :
    grille[len(grille)-1][len(grille)-1]=5
    pion=np.zeros(2)
    pion[0]=len(grille)-1
    pion[1]=len(grille)-1
    return grille, pion


def movePown1(grid,pos):
    step=str(input("Où voulez vous aller ?\n"))
    x=int(pos[0])
    y=int(pos[1])
    if (step == "d") and (y!=len(grid)) :
        grid[x][y+1]=9
        grid[x][y]=4
        pos[1]=y+1
    elif (step == "q") and (x!=0) :
        grid[x][y-1]=9
        grid[x][y]=4
        pos[1]=y-1
    elif (step == "s") and (y!=0) :
        grid[x+1][y]=9
        grid[x][y]=4
        pos[0]=x+1
    elif (step == "z") and (y!=len(grid)) :
        if (grid[x-1][y]==2) :
            bonus.bombeAutour(grid,pos)
            grid[x-1][y]=9
            grid[x][y]=4
            pos[0]=x+-1
        else :
            grid[x-1][y]=9
            grid[x][y]=4
            pos[0]=x+-1
    else :
        print("Impossible de se déplacer ici\n Recommencez\n")
        movePown1(grid,pos)
    return grid, pos


def movePown2(grid,pos):
    step=str(input("Où voulez vous aller ?\n"))
    x=int(pos[0])
    y=int(pos[1])
    if (step == "d") and (y!=len(grid)) :
        grid[x][y+1]=5
        grid[x][y]=0
        pos[1]=y+1
    elif (step == "q") and (x!=0) :
        grid[x][y-1]=5
        grid[x][y]=0
        pos[1]=y-1
    elif (step == "s") and (y!=0) :
        grid[x+1][y]=5
        grid[x][y]=0
        pos[0]=x+1
    elif (step == "z") and (y!=len(grid)) :
        grid[x-1][y]=5
        grid[x][y]=0
        pos[0]=x+-1
    else :
        print("Impossible de se déplacer ici\n Recommencez\n")
        movePown1(grid,pos)
    return grid, pos
        
          
def multimove1(grid,pos) :
    pm=0
    while (pm < 3) :
        movePown1(grid,pos)
        afficherGrille(grid)
        pm+=1
    return grid

def multimove2(grid,pos) :
    pm=0
    while (pm < 3) :
        movePown2(grid,pos)
        afficherGrille(grid)
        pm+=1
    return grid