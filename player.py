import pygame
import math
import random
pygame.init()


class PlayerActive(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("mob.png")  # USE S in surface s capital
        self.rect = self.image.get_rect()  #rect is py game object for storing rectanle codinates

        self.rect.x = 100
        self.rect.y = 100

        self.speed = 5
        self.Spawn_delay = 0
        self.Spawn_delay_max = 30
        self.ammo = []
        self.bullets = pygame.sprite.Group()
        self.cd = 10
        self.cdmax = 10
        self.isAlive = True

