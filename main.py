import pygame
bg = pygame.image.load("back.jpg")
ico = pygame.image.load("moon.png")
win = pygame.display.set_mode((1024,500))
pygame.display.set_caption("Mazer: The Legacy Unfolded")
pygame.display.set_icon(ico)

class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False

man = player(250,250,15,25)

def winfill():
    win.blit(bg,(0,0))
    pygame.draw.rect(win,(255,120,45),(man.x,man.y,man.width,man.height))
    pygame.display.update()

run = True

while run:
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if man.x>0:
            man.x-=man.vel
    if keys[pygame.K_RIGHT]:
        if man.x<1005:
            man.x+=man.vel
    if keys[pygame.K_UP]:
        if man.y>0:
            man.y-=man.vel
    if keys[pygame.K_DOWN]:
        if man.y<480:
            man.y+=man.vel
    winfill()
    clock.tick(60)

    
