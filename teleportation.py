import pygame
import numpy as np

class Teleportation(pygame.sprite.Sprite):
    
    def __init__(self, x, y, a, grille):
        self.grille = grille
        self.image = pygame.image.load(a)
        self.position = self.image.get_rect()
        self.position.x = x
        self.position.y = y
        self.activer = 1
        
    def teleporte(self, tp, pion):
        if (pion.position.x == self.position.x and pion.position.y == self.position.y):
             pion.position.x = tp.position.x
             pion.position.y = tp.position.y
    
    def deplacer(self,x,y):
        self.position.x = x
        self.position.y = y