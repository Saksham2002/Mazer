import pygame
import math
import util
import random

spawnCD = 0
spawnCDMAX = 200

def spawn():
    global spawnCD, spawnCDMAX
    spawnCD -= 1
    if spawnCD <= 0:
        newenemy = Enemy()
        Enemy.enemies.add(newenemy)
        spawnCD = spawnCDMAX
        newenemy.rect.x = random.randrange(-100, -50)
        newenemy.rect.y = random.randrange(-50, 650)

class Enemy(pygame.sprite.Sprite):
    enemies = pygame.sprite.Group()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/mob.png")
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
    def disp(self,k,player):
        xdiff = (player.rect.x + player.rect.width/2) - self.rect.x + self.rect.width/2
        #giving target input from mouse left and right keys
        ydiff = (player.rect.y + player.rect.height/2) - self.rect.y + self.rect.height/2
        pygame.draw.rect(k,(255,0,0),(xdiff-14,ydiff-22,20,5))
        pygame.draw.rect(k,(0,255,0),(xdiff-14,ydiff-22,20,5))
        pygame.display.update()
    def takedamage(self):
        self.health -= 1
        if self.health <= 0:
            self.destroy()


    def destroy(self):
        self.kill()  #pyagme destroys function

    def update(self, player):
        k = self.aim_player(player)
        return k
