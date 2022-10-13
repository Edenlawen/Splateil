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
from teleportation import Teleportation
from ligne import Ligne
from ligneV import LigneV

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

piegeB = Bombe(415+5*25, 235+5*25, grille_jeu)
piegeB.random()
#piegeB.invisible()

tp_bleu = Teleportation(415+525, 235+525, 'images/TPB.png', grille_jeu)
tp_bleu.random()

tp_orange = Teleportation(415+525, 235+525, 'images/TPO.png', grille_jeu)
tp_orange.random()

test_ligne = Ligne(415, 235, grille_jeu)
test_ligne.random()

test_ligne2 = LigneV(415, 235, grille_jeu)
test_ligne2.random()



ligneV = LigneV(415, 235, grille_jeu)
ligneV.random()

piegeL = Ligne(415, 235, grille_jeu)
piegeL.random()
#piegeL.invisible()

file = 'song/musique.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)


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
        
    screen.blit(test_ligne.image, test_ligne.position)
    if (pion_vert.position.x == test_ligne.position.x and pion_vert.position.y == test_ligne.position.y):
        test_ligne.explosion(2)
    if (pion_rouge.position.x == test_ligne.position.x and pion_rouge.position.y == test_ligne.position.y):
        test_ligne.explosion(1)
    screen.blit(test_ligne2.image, test_ligne2.position)
    if (pion_vert.position.x == test_ligne2.position.x and pion_vert.position.y == test_ligne2.position.y):
        test_ligne2.explosion(0)
    if (pion_rouge.position.x == test_ligne2.position.x and pion_rouge.position.y == test_ligne2.position.y):
        test_ligne2.explosion(0)
        
    screen.blit(ligneV.image, ligneV.position)
    if (pion_vert.position.x == ligneV.position.x and pion_vert.position.y == ligneV.position.y):
        ligneV.explosion(2)
    if (pion_rouge.position.x == ligneV.position.x and pion_rouge.position.y == ligneV.position.y):
        ligneV.explosion(1)
      
    screen.blit(piegeB.image, piegeB.position)
    if (pion_vert.position.x == piegeB.position.x and pion_vert.position.y == piegeB.position.y):
        piegeB.explosion(0)
    if (pion_rouge.position.x == piegeB.position.x and pion_rouge.position.y == piegeB.position.y):
        piegeB.explosion(0)
    screen.blit(piegeL.image, piegeL.position)
    if (pion_vert.position.x == piegeL.position.x and pion_vert.position.y == piegeL.position.y):
        piegeL.explosion(0)
    if (pion_rouge.position.x == piegeL.position.x and pion_rouge.position.y == piegeL.position.y):
        piegeL.explosion(0)
        
    screen.blit(tp_bleu.image,tp_bleu.position)
    screen.blit(tp_orange.image,tp_orange.position)
    if(pion_rouge.position.x == tp_orange.position.x and pion_rouge.position.y == tp_orange.position.y):
        tp_orange.teleporte(tp_bleu,pion_rouge)
    #elif(pion_rouge.position.x == tp_bleu.position.x and pion_rouge.position.y == tp_bleu.position.y):
        #tp_bleu.teleporte(tp_orange,pion_rouge)
    elif(pion_vert.position.x == tp_bleu.position.x and pion_vert.position.y == tp_bleu.position.y):
        tp_bleu.teleporte(tp_orange,pion_vert)
    #elif(pion_vert.position.x == tp_orange.position.x and pion_vert.position.y == tp_orange.position.y):
        #tp_orange.teleporte(tp_bleu,pion_vert)
    
    #screen.blit(test_teleporte.image,test_teleporte.position)
    #screen.blit(test_teleporte2.image,test_teleporte2.position) 
    
    whitecase=grille_jeu.nb_case_blanche()
    greencase=grille_jeu.nb_case_verte()
    redcase=grille_jeu.nb_case_rouge()
    
    white=(253,239,228)
    vert=(4,87,51)
    rouge=(116,0,38)
    black=(0,0,0)
    fond_test=pygame.font.Font('freesansbold.ttf', 32)
    redwin=fond_test.render('Le joueur Rouge a gagné',True,rouge,white)
    greenwin=fond_test.render('Le joueur Vert a gagné',True,vert,white)
    tie=fond_test.render('Egalité !',True,black,white)
    
    redScore=fond_test.render('score rouge : ' + str(redcase),True,rouge,white)
    redDisplay=redScore.get_rect()
    redDisplay.center=(270,300)
    screen.blit(redScore,redDisplay)
    
    greenScore=fond_test.render('score vert  : ' + str(greencase),True,vert,white)
    greenDisplay=greenScore.get_rect()
    greenDisplay.center=(800,300)
    screen.blit(greenScore,greenDisplay)
    
    screen.blit(pion_vert.image, pion_vert.position)
    screen.blit(pion_rouge.image, pion_rouge.position)
    
    if whitecase==0 and greencase<redcase :
        textdisplay=redwin.get_rect()
        textdisplay.center=(530,150)
        screen.blit(redwin,textdisplay)
        
    if whitecase==0 and greencase>redcase :
        textdisplay=greenwin.get_rect()
        textdisplay.center=(530,150)
        screen.blit(greenwin,textdisplay)
        
    if whitecase==0 and greencase==redcase :
        textdisplay=tie.get_rect()
        textdisplay.center=(530,150)
        screen.blit(tie,textdisplay)
    
    pygame.display.flip() 
    
    
    
    for event in pygame.event.get():
        
        
        
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        if whitecase!=0 :
        
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_r:
                        grille_jeu.listecase[35].change_color(1)
                elif event.key == pygame.K_b:
                        grille_jeu.listecase[35].change_color(0)
                elif event.key == pygame.K_v:
                        grille_jeu.listecase[35].change_color(2)
                elif event.key == pygame.K_F5:
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
                    
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pion_rouge.move_gauche()
                elif event.key == pygame.K_RIGHT:
                    pion_rouge.move_droite()
                elif event.key == pygame.K_UP:
                    pion_rouge.move_up()
                elif event.key == pygame.K_DOWN:
                    pion_rouge.move_down()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pion_vert.move_gauche()
                elif event.key == pygame.K_d:
                    pion_vert.move_droite()
                elif event.key == pygame.K_z:
                    pion_vert.move_up()
                elif event.key == pygame.K_s:
                    pion_vert.move_down()
            
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE:
                    if grille_jeu.tour_joueur == 0:
                        grille_jeu.tour_joueur = 1
                    elif grille_jeu.tour_joueur == 1:
                        grille_jeu.tour_joueur = 0
                
        if event.type == pygame.KEYDOWN :        
            if event.key == pygame.K_F5:
                pion_rouge.position.x = 640
                pion_rouge.position.y = 460
                pion_vert.position.x = 415
                pion_vert.position.y = 235
                
                test_bombe.reactiver()
                test_bombe.random()
                test_bombe2.reactiver()
                test_bombe2.random()
               
                tp_bleu.random()
                tp_orange.random()
               
                test_ligne.reactiver()
                test_ligne.random()
                ligneV.reactiver()
                ligneV.random()
                
                piegeB.reactiver()
                piegeB.random()
                #piegeB.invisible()
                piegeL.reactiver()
                piegeL.random()
                #piegeL.invisible()
                test_ligne2.reactiver()
                test_ligne2.random()
                for k in range(0,100):
                    grille_jeu.listecase[k].change_color(0)
                
        
            