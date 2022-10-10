# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 19:37:04 2022

@author: mahor
"""

import pygame

class Pion(pygame.sprite.Sprite):
    def __init__(self, a, x, y):
        
        self.vitesse = 25
        self.image = pygame.image.load(a)
        self.position = self.image.get_rect()
        self.position.x = x
        self.position.y = y
  
    def move_droite(self):
        if self.position.x < 640:
            self.position.x = self.position.x + self.vitesse
    def move_gauche(self):
        if self.position.x > 415:
            self.position.x = self.position.x - self.vitesse
    def move_up(self):
        if self.position.y > 235 :
            self.position.y = self.position.y - self.vitesse
    def move_down(self):
        if self.position.y < 460 :
            self.position.y = self.position.y + self.vitesse
    