# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:05:43 2022

@author: mahor
"""

import pygame
pygame.init()

from grille import Grille
from pion import Pion
from Bombe import Bombe

pygame.display.set_caption("Splateil")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load('images/beige.jpg')
running = True

grille_jeu = Grille(0, 0, 415, 235, 0)
pion_vert = Pion('images/case/PionV.png', 415, 235)
pion_rouge = Pion('images/case/PionR.png', 640, 460)

test_bombe = Bombe(415+5*25, 235+5*25, grille_jeu)
test_bombe.random()

test_bombe2 = Bombe(415+5*25, 235+5*25, grille_jeu)
test_bombe2.random()
#test_bombe.invisible()


while running:
    
    screen.blit(background,(0,0))
    screen.blit(grille_jeu.listecase[0].image, grille_jeu.listecase[0].position)
    
    for k in range(0,100):
        screen.blit(grille_jeu.listecase[k].image, grille_jeu.listecase[k].position)
        if (grille_jeu.listecase[k].position.x==pion_rouge.position.x and grille_jeu.listecase[k].position.y == pion_rouge.position.y):
            grille_jeu.listecase[k].change_color(1)
        if (grille_jeu.listecase[k].position.x==pion_vert.position.x and grille_jeu.listecase[k].position.y == pion_vert.position.y):
            grille_jeu.listecase[k].change_color(2)
   
    screen.blit(test_bombe.image, test_bombe.position)
    screen.blit(test_bombe2.image, test_bombe2.position)
    if (pion_vert.position.x == test_bombe.position.x and pion_vert.position.y == test_bombe.position.y):
        test_bombe.explosion(2)
    if (pion_rouge.position.x == test_bombe.position.x and pion_rouge.position.y == test_bombe.position.y):
        test_bombe.explosion(1)
    if (pion_vert.position.x == test_bombe2.position.x and pion_vert.position.y == test_bombe2.position.y):
        test_bombe2.explosion(2)
    if (pion_rouge.position.x == test_bombe2.position.x and pion_rouge.position.y == test_bombe2.position.y):
        test_bombe2.explosion(1)
    
    screen.blit(pion_vert.image, pion_vert.position)
    screen.blit(pion_rouge.image, pion_rouge.position)
    
    
    pygame.display.flip() 
    
    
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                    grille_jeu.listecase[35].change_color(1)
            elif event.key == pygame.K_b:
                    grille_jeu.listecase[35].change_color(0)
            
                    grille_jeu.listecase[35].change_color(2)
            elif event.key == pygame.K_F5:
                print('F5')
                pion_rouge.position.x = 640
                pion_rouge.position.y = 460
                pion_vert.position.x = 415
                pion_vert.position.y = 235
                test_bombe.reactiver()
                test_bombe.random()
                test_bombe2.reactiver()
                test_bombe2.random()
                for k in range(0,100):
                   grille_jeu.listecase[k].change_color(0)
                   
               
        
        if (grille_jeu.tour_joueur == 0):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pion_rouge.move_gauche()
                elif event.key == pygame.K_RIGHT:
                    pion_rouge.move_droite()
                elif event.key == pygame.K_UP:
                    pion_rouge.move_up()
                elif event.key == pygame.K_DOWN:
                    pion_rouge.move_down()
        
        if (grille_jeu.tour_joueur == 1):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pion_vert.move_gauche()
                elif event.key == pygame.K_RIGHT:
                    pion_vert.move_droite()
                elif event.key == pygame.K_UP:
                    pion_vert.move_up()
                elif event.key == pygame.K_DOWN:
                    pion_vert.move_down()
        
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                if grille_jeu.tour_joueur == 0:
                    grille_jeu.tour_joueur = 1
                elif grille_jeu.tour_joueur == 1:
                    grille_jeu.tour_joueur = 0
                
        
            