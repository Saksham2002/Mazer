import os
import random
import pygame,util,pygame_menu
from design import des
from enemy import Enemy
from enemy import spawn
# initialising pygame
pygame.init()
screen = pygame.display.set_mode((1024,680))
ico = pygame.image.load("moon.png")
pygame.display.set_icon(ico)
##########################################         MAZER Ver 2.0
bg = pygame.image.load("back.jpg")
fo = pygame.font.Font("diodrum.woff",25)
ban = pygame.font.Font("arc.ttf",50)
qs = pygame.font.Font("arc.ttf",20)
mob = pygame.image.load("mob.png").convert()
pygame.mixer.music.load("back2.mp3")
pygame.mixer.music.play(-1,2.0)
scor,sflag= 0,0
sp = 10
class Player(object):
    global reap
    
    def __init__(self):
        self.image = pygame.image.load("reap.png")  # reaper
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 550
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
    def up(self):
        pygame.display.update(self.rect)
# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 3,3)

# Set up the display
pygame.display.set_caption("Mazer: The Legacy Unfolded")
clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player
en =  Enemy()
en1 = Enemy()
en2 = Enemy()
en3 = Enemy()
en.speed = 5
en1.speed = 4
en2.speed = 6
en3.speed = 10
enemies = Enemy.enemies
x = y = 0
for row in des:
    for col in row:
        if col == "X":
            Wall((0.2*x, 0.17*y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 5,5)
        x += 16
    y += 16
    x = 0
def status():
    if sflag!=1:
        k = pygame.font.Font.render(qs,"MUSIC  PLAYING", 1,(0, 204, 0),True)
        screen.blit(k,(850,570))
    else:
        k = pygame.font.Font.render(qs,"MUSIC  PAUSED", 1,(255, 0, 0),True)
        screen.blit(k,(850,570))
def start_the_game():
    # Do the job here !
    running = True
    global scor,sflag
    while running:
        
        key = pygame.key.get_pressed()
        clock.tick(60)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
        
        # Move the player if an arrow key is pressed
        if key[pygame.K_q]:
            break
        if key[pygame.K_p]:
            pygame.mixer.music.pause()
            sflag = 1
        if key[pygame.K_m]:
            pygame.mixer.music.unpause()
            sflag = 0
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            player.move(-sp, 0)
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            player.move(sp, 0)
        if key[pygame.K_UP] or key[pygame.K_w]:
            player.move(0, -sp)
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            player.move(0, sp)
        playerCollision = pygame.sprite.spritecollide(player,enemies,False)
        # this is the list who is colliding with player
        for enemy in playerCollision:
            enemy.destroy()
        
        # Draw the scene
        screen.blit(bg,(-1120,-320))
        i = 0
        for wall in walls:
            if i%2==0:
                pygame.draw.rect(screen, (82, 99, 255), wall.rect)
            else:
                pygame.draw.rect(screen, (255, 169, 48), wall.rect)
            i+=1
        screen.blit(player.image, player.rect)
        Sco = pygame.font.Font.render(fo,"Score: "+str(scor), 5,(255,255,255),True)
        bn = pygame.font.Font.render(ban,"MAZER", 1,(255,255,255),True)
        qd = pygame.font.Font.render(qs,"PRESS Q TO PAUSE", 1,(255,255,255),True)
        screen.blit(Sco,(840,55))
        screen.blit(bn,(840,5))
        screen.blit(qd,(850,640))
        enemies.update(player)
        enemies.draw(screen)
        en.disp(screen,en1)
        t = pygame.time.get_ticks()
        if t%64 ==0:
            scor+=1
        player.up()
        screen.fill((0,0,0))
        spawn()
        status()
font = pygame_menu.font.FONT_8BIT
mazer = pygame_menu.themes.Theme(title_font_size= 55,title_font_color=(255,255,255),title_background_color= (0, 51, 102),widget_font=font,title_font=font,title_bar_style= pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY)
st  = pygame_menu.baseimage.BaseImage("start.png",drawing_mode=101, drawing_offset=(0, 0), load_from_file=True)
mazer.background_color = st
menu = pygame_menu.Menu(680, 1024,theme=mazer,title='MAZER')
menu.add_button('Press Enter', start_the_game)
menu.mainloop(screen)