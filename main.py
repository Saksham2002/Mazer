import pygame
bg = pygame.image.load("back.jpg")
ico = pygame.image.load("icon.png")
win = pygame.display.set_mode((1024,500))
pygame.display.set_caption("Mazer: The Legacy Unfolded")
pygame.display.set_icon(ico)

x,y,wid,hei,vel=250,250,15,25,10
run = True
def winfill():
    win.blit(bg,(0,0))
    pygame.draw.rect(win,(255,120,45),(x,y,wid,hei))
    pygame.display.update()

while run:
    clock = pygame.time.Clock()

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            run = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x>0:
            x-=vel
    if keys[pygame.K_RIGHT]:
        if x<1000:
            x+=vel
    if keys[pygame.K_UP]:
        if y>0:
            y-=vel
    if keys[pygame.K_DOWN]:
        if y<480:
            y+=vel
    winfill()
    clock.tick(60)

    
