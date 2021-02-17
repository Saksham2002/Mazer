import os
import random
import pygame,util
from design import des
from enemy import Enemy
# initialising pygame
pygame.init()
ico = pygame.image.load("moon.png")
pygame.display.set_icon(ico)
##########################################         MAZER Ver 2.0
st = pygame.image.load("start.png")
bg = pygame.image.load("back.jpg")
fo = pygame.font.Font("diodrum.woff",25)
ban = pygame.font.Font("arc.ttf",50)
mob = pygame.image.load("mob.png")
pygame.mixer.music.load("back.mp3")
pygame.mixer.music.play(-1,0.0)
scor = 0
sp = 10
class Player(object):
    global reap
    
    def __init__(self):
        self.image = pygame.image.load("reap1.png")  # reaper
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 600
    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 3,3)

# Set up the display
pygame.display.set_caption("Mazer: The Legacy Unfolded")
screen = pygame.display.set_mode((1024,680))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player
en = Enemy()
en1 = Enemy()
en2 = Enemy()
en.speed = 5
en1.speed = 4
en2.speed = 6  
enemies = pygame.sprite.Group()
enemies.add(en)
enemies.add(en1)
enemies.add(en2)
x = y = 0
for row in des:
    for col in row:
        if col == "X":
            Wall((0.2*x, 0.17*y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True

while running:
    
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_q]:
        running = True
    if key[pygame.K_q]:
        running = False
    if key[pygame.K_LEFT]:
        player.move(-sp, 0)
    if key[pygame.K_RIGHT]:
        player.move(sp, 0)
    if key[pygame.K_UP]:
        player.move(0, -sp)
    if key[pygame.K_DOWN]:
        player.move(0, sp)
    playerCollision = pygame.sprite.spritecollide(player,enemies,False)
    # this is the list who is colliding with player
    for enemy in playerCollision:
        enemy.destroy()
    
    # Draw the scene
    screen.blit(bg,(-1120,0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 154, 153), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    screen.blit(player.image, player.rect)
    Sco = pygame.font.Font.render(fo,"Score: "+str(scor), 1,(255,255,255),True)
    bn = pygame.font.Font.render(ban,"MAZER", 1,(255,255,255),True)
    screen.blit(Sco,(840,55))
    screen.blit(bn,(840,5))
    enemies.update(player)
    enemies.draw(screen)
    pygame.display.flip()