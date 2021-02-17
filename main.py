import pygame
from design import des
pygame.init()
bg = pygame.image.load("back.png")
ico = pygame.image.load("moon.png")
win = pygame.display.set_mode((1200,500))
pygame.display.set_caption("Mazer: The Legacy Unfolded")
pygame.display.set_icon(ico)
fo = pygame.font.Font("diodrum.woff",25)
mob = pygame.image.load("mob.png")
reap = pygame.image.load("reap1.png")
scor = 0

class maze:
    def __init__(self):
        self.sw = 4
        self.sh = 2

    def drawmaze(self):
        r,c=0,0
        for y in range(0,501,2):
            c = 0
            for x in range(0,1025,4):
                if des[r][c]== "X":
                    pygame.draw.rect(win,(255, 154, 153),(x,y,self.sw,self.sh))
                else:
                    pass
                c+=1
            r+=1
    def iscolliding(self,x,y):
        pass

ob = maze()
ob.drawmaze()     

class player:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.left = False
        self.right = False

man = player(28,14,15,5)

def winfill():
    win.blit(bg,(0,0))
    ob = maze()
    ob.drawmaze()
    win.blit(reap,(man.x,man.y))
    Sco = pygame.font.Font.render(fo,"Score: "+str(scor), 1,(255,255,255),True)
    pygame.draw.rect(win,(255,120,45),(man.x+8,man.y+16,4,2))
    win.blit(Sco,(1040,5))
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
            if des[(man.x-8)//4][(man.y+8)//2] != "X":
                print(man.x,man.y)
                man.x-=man.vel
            else:
                pass
    elif keys[pygame.K_RIGHT]:
        if man.x<950:
            if des[(man.x+8)//4][(man.y+8)//2] != "X":
                man.x+=man.vel
            else:
                pass
    elif keys[pygame.K_UP]:
        if man.y>10:
            if des[(man.x+8)//4][(man.y-8)//2] != "X":
                man.y-=man.vel
            else:
                pass
    elif keys[pygame.K_DOWN]:
        if man.y<470:
            if des[(man.x+8)//4][(man.y+16)//2] != "X":
                man.y+=man.vel
            else:
                pass
    elif keys[pygame.K_q]:
        run = False
    winfill()
    clock.tick(240)

    
