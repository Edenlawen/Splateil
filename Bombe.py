# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:20:08 2022

@author: mahor
"""
import pygame
import numpy as np

class Bombe(pygame.sprite.Sprite):
    
    def __init__(self, x, y, grille):
        self.grille = grille
        self.image = pygame.image.load('images/bomb.png')
        self.position = self.image.get_rect()
        self.position.x = x
        self.position.y = y
        self.activer = 1

    def explosion(self, color):
        if self.activer == 1:
            for k in range (0,100):
                if (self.grille.listecase[k].position.x == self.position.x and self.grille.listecase[k].position.y == self.position.y):
                  a = k
            for n in range (-1,2):
                for i in range(-1,2):
                    if a+i + 10*n<100:
                        self.grille.listecase[a+i + 10*n].change_color(color)
            self.image = pygame.image.load('images/vide.png')
            self.activer = 0
    
    def reactiver(self):
        self.activer = 1
        self.image = pygame.image.load('images/bomb.png')
        
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
    
            
        