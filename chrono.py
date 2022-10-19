import pygame

class Chrono():
    def __init__(self):
        self.time=pygame.time.get_ticks()
    def chrono(self) :
        return self.time