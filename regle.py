# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:17:04 2022

@author: mahor
"""

import pygame

class Regle(pygame.sprite.Sprite):
            
        def __init__(self):
            self.image = pygame.image.load('images/regle.png')
            self.position = self.image.get_rect()
            self.position.x = 0
            self.position.y = 500
            