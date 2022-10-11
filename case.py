# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:41:26 2022

@author: mahor
"""

import pygame

class Case(pygame.sprite.Sprite):
    
    def __init__(self, x, y, xpos, ypos, col):
        
        self.x = x
        self.y = y
        self.color = col
        if (self.color == 0):
            self.image = pygame.image.load('images/case/blanc.png')
        elif (self.color == 1):
            self.image = pygame.image.load('images/case/rose.png')
        elif (self.color == 2):
            self.image = pygame.image.load('images/case/verte.png')    
        self.position = self.image.get_rect()
        self.position.x = xpos
        self.position.y = ypos
        self.pleine = 0

        
    def change_color(self, color):
        self.color = color
        if (self.color == 0):
            self.image = pygame.image.load('images/case/blanc.png')
            self.color = 0
        elif (self.color == 1):
            self.image = pygame.image.load('images/case/rose.png')
            self.color = 1
        elif (self.color == 2):
            self.image = pygame.image.load('images/case/verte.png')
            self.color = 2
            