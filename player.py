import random
import math
import pygame

class player:
    def __init__(self,scre,ht=5):
        self.scr = scre
        self.health = ht
        self.x = random.randrange(900)
        self.y = random.randrange(500)
    def bardisp(self):
        pygame.draw.rect(self.scr,(255,0,0),(xdiff-14,ydiff-22,20,5))
        pygame.draw.rect(self.scr,(0,255,0),(xdiff-14,ydiff-22,20,5))
        pygame.display.update()
    def playdisp(self):
         