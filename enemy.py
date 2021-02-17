import pygame
import math
import util


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("mob.png")
        self.rect = self.image.get_rect()  #getting co-ordinates
        self.speed = 3
        self.health = 5

    def aim_player(self, player):

        xdiff = (player.rect.x + player.rect.width/2) - self.rect.x + self.rect.width/2
        #giving target input from mouse left and right keys
        ydiff = (player.rect.y + player.rect.height/2) - self.rect.y + self.rect.height/2

        magnitude = math.sqrt(float(xdiff ** 2 + ydiff ** 2))  #pythogoruss

        numframes = int(magnitude / self.speed)
        try:
            xmove = xdiff/numframes
            ymove = ydiff/numframes  #only need this variable locally
        except:
            return 1
        self.rect.x += xmove
        self.rect.y += ymove
    def takedamage(self):
        self.health -= 1
        if self.health <= 0:
            self.destroy()


    def destroy(self):
        self.kill()  #pyagme destroys function

    def update(self, player):
        k = self.aim_player(player)
        return k
