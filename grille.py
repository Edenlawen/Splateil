# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:06:06 2022

@author: mahor
"""

import pygame
from case import Case

class Grille(pygame.sprite.Sprite):
    
    def __init__(self, x, y, xpos, ypos, col):
        self.tour_joueur = 1
        self.listecase = []
        for k in range(0,10):
            for n in range(0,10):
                self.listecase.append(Case(n, k, xpos+25*n, ypos + 25*k, 0))
       

              