from tkinter import X
import deplacement as dp
import numpy as np

def teleportation1(grid,pos) :
    x1=pos[0]
    y1=pos[1]
    x2=np.random.randint(0,len(grid)-1)
    y2=np.random.randint(0,len(grid)-1)
    grid[x1][y1]=4
    pos[0]=x2
    pos[2]=y2
    return grid, pos
    