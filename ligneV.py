# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 08:32:56 2022

@author: mahor
"""

import pygame
import numpy as np

class LigneV(pygame.sprite.Sprite) :
    
    def __init__(self, x, y, grille):
        self.grille = grille
        self.image = pygame.image.load('images/verti.png')
        self.position = self.image.get_rect()
        self.position.x = x
        self.position.y = y
        self.activer = 1
        
        
    def explosion(self, color):
        if self.activer == 1:
            for k in range (0,100):
                if (self.grille.listecase[k].position.x == self.position.x and self.grille.listecase[k].position.y == self.position.y):
                  a = k%10
            for i in range(0,10):
                    self.grille.listecase[i*10 + a].change_color(color)
            self.image = pygame.image.load('images/vide.png')
            self.activer = 0
    
    def reactiver(self):
        self.activer = 1
        self.image = pygame.image.load('images/verti.png')
        
    def invisible(self):
        self.image = pygame.image.load('images/case/blanc.png')
        
    def deplacer(self,x,y):
        self.position.x = x
        self.position.y = y
        
    def random(self):
        a = 0
        while a == 0:
            a = np.random.randint(1,9)
            b = np.random.randint(1,10)
            
            if self.grille.listecase[a+10*b].pleine == 0:
                self.deplacer(415+a*25, 235+b*25)
                a = 1
                self.grille.listecase[a+10*b].pleine = 1
                