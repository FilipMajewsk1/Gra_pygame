# -*- coding: utf-8 -*-

import sys, pygame, random
from pygame.locals import *

pygame.init()

pygame.display.set_mode((800,600))
pygame.display.set_caption("stateczki")

okienko = pygame.display.get_surface()

statek = pygame.image.load("./statek1.gif")
sXY = statek.get_rect()
sXY.x=20
sXY.y=300

lisc = pygame.image.load("./lisc.gif")
lXY = lisc.get_rect()
lXY.x=750
lXY.y=-100

enemy1 = pygame.image.load("./enemy.gif")
e1XY = enemy1.get_rect()
e1XY.x=random.randint(1000,1000)
e1XY.y=random.randint(20,180)

enemy2 = pygame.image.load("./enemy.gif")
e2XY = enemy2.get_rect()
e2XY.x=random.randint(1000,1000)
e2XY.y=random.randint(200,380)

enemy3 = pygame.image.load("./enemy.gif")
e3XY = enemy3.get_rect()
e3XY.x=random.randint(1000,1000)
e3XY.y=random.randint(400,580)

enemy4 = pygame.image.load("./enemy2.gif")
e4XY = enemy4.get_rect()
e4XY.x=random.randint(1000,1000)
e4XY.y=random.randint(400,580)

pocisk1 = pygame.Surface((25,4))
pocisk1.fill((200,100,150))
p1XY = pocisk1.get_rect()
p1XY.x=1200
p1XY.y=500

pocisk2 = pygame.Surface((25,4))
pocisk2.fill((200,100,150))
p2XY = pocisk2.get_rect()
p2XY.x=1200
p2XY.y=500

pocisk3 = pygame.image.load("./rakieta.gif")
p3XY = pocisk3.get_rect()
p3XY.x=1200
p3XY.y=sXY.y+40

poz1 = pygame.image.load("./ez.gif")
pz1XY = poz1.get_rect()
pz1XY.x=350
pz1XY.y=80

poz2 = pygame.image.load("./med.gif")
pz2XY = poz2.get_rect()
pz2XY.x=350
pz2XY.y=250

poz3 = pygame.image.load("./hard.gif")
pz3XY = poz3.get_rect()
pz3XY.x=350
pz3XY.y=430

napis= pygame.image.load("./gameover.gif")
nXY = napis.get_rect()
nXY.x=285
nXY.y=250

HP = pygame.image.load("./Hp.gif")
hpXY = HP.get_rect()
hpXY.x=65
hpXY.y=10

score = pygame.image.load("./score.gif")
scXY = score.get_rect()
scXY.x=570
scXY.y=10

hp1 = pygame.image.load("./serce.gif")
hp1XY = hp1.get_rect()
hp1XY.x=100
hp1XY.y=10

hp2 = pygame.image.load("./serce.gif")
hp2XY = hp2.get_rect()
hp2XY.x=130
hp2XY.y=10

hp3 = pygame.image.load("./serce.gif")
hp3XY = hp3.get_rect()
hp3XY.x=160
hp3XY.y=10

up = pygame.image.load("./serce.gif")
upXY = up.get_rect()
upXY.x=random.randint(150,750)
upXY.y=1000

sy=10

upx=0
upy=0

e1x=0
e2x=0
e3x=0
e4x=0

p1x=40
p2x=40
p3x=10

v1=2
v2=3

hp=0
pkt=0
diff=0

czcionka=pygame.font.Font("./czcionka.ttf",40)
def punktuj():
    tekst=czcionka.render(str(pkt),True,(220,100,150))
    tXY=tekst.get_rect()
    tXY.y=7
    tXY.x=690
    okienko.blit(tekst,tXY)

pygame.display.flip()

fps = pygame.time.Clock()
while 1:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == QUIT:
            sys.exit(0)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and sXY.y > 3:
        sXY.y-=sy
        p3XY.y-=sy
    if keys[pygame.K_s] and sXY.y < 517:
        sXY.y+=sy
        p3XY.y+=sy
    if keys[pygame.K_d] and p1XY.x > 825 and p2XY.x > 825:
        p1XY.x=sXY.x
        p1XY.y=sXY.y+5
        p2XY.x=sXY.x
        p2XY.y=sXY.y+75
    if keys[pygame.K_SPACE] and p3XY.x > 800:
        p3XY.x=sXY.x

    if hp==2:
        upy=5
    if upXY.y<=(-100):
        upy=0
    if p1XY.colliderect(upXY) or p2XY.colliderect(upXY) or p3XY.colliderect(upXY):
        upXY.y=(-99)
        hp-=1

        
    if e1XY.x<=0:
        e1XY.x=random.randint(850,950)
        e1XY.y=random.randint(20,180)
        if diff==1:
            e1x=random.randint(v1,v2)
        if diff==2:
            e1x=random.randint(v1+1,v2+1)
        if diff==3:
            e1x=random.randint(v1+2,v2+2)
        hp+=1
    if e2XY.x<=0:
        e2XY.x=random.randint(850,950)
        e2XY.y=random.randint(200,380)
        if diff==1:
            e2x=random.randint(2,3)
        if diff==2:
            e2x=random.randint(3,4)
        if diff==3:
            e2x=random.randint(4,5)
        hp+=1
    if e3XY.x<=0:
        e3XY.x=random.randint(850,950)
        e3XY.y=random.randint(400,560)
        if diff==1:
            e3x=random.randint(2,3)
        if diff==2:
            e3x=random.randint(3,4)
        if diff==3:
            e3x=random.randint(4,5)
        hp+=1
    if e4XY.x<=0:
        e4XY.x=random.randint(2000,2200)
        e4XY.y=random.randint(50,560)
        if diff==1:
            e4x=4
        if diff==2:
            e4x=5
        if diff==3:
            e4x=6
        hp+=1


    if p1XY.colliderect(pz1XY) or p2XY.colliderect(pz1XY):
        pz1XY.y=1000
        pz2XY.y=1000
        pz3XY.y=1000
        e1x=random.randint(v1,v2)
        e2x=random.randint(v1,v2)
        e3x=random.randint(v1,v2)
        e4x=4
        diff=1
    if p1XY.colliderect(pz2XY) or p2XY.colliderect(pz2XY):
        pz1XY.y=1000
        pz2XY.y=1000
        pz3XY.y=1000
        e1x=random.randint(v1+1,v2+1)
        e2x=random.randint(v1+1,v2+1)
        e3x=random.randint(v1+1,v2+1)
        e4x=5
        diff=2
    if p1XY.colliderect(pz3XY) or p2XY.colliderect(pz3XY):
        pz1XY.y=1000
        pz2XY.y=1000
        pz3XY.y=1000
        e1x=random.randint(v1+2,v2+2)
        e2x=random.randint(v1+2,v2+2)
        e3x=random.randint(v1+2,v2+2)
        e4x=6
        diff=3

    if p1XY.colliderect(e1XY) or p2XY.colliderect(e1XY) or p3XY.colliderect(e1XY):
        e1XY.y=random.randint(20,180)
        e1XY.x=random.randint(850,950)
        if diff==1:
            e1x=random.randint(v1,v2)
        if diff==2:
            e1x=random.randint(v1+1,v2+1)
        if diff==3:
            e1x=random.randint(v1+2,v2+2)
        pkt+=10
    if p1XY.colliderect(e2XY) or p2XY.colliderect(e2XY) or p3XY.colliderect(e2XY):
        e2XY.y=random.randint(200,380)
        e2XY.x=random.randint(850,950)
        if diff==1:
            e2x=random.randint(v1,v2)
        if diff==2:
            e2x=random.randint(v1+1,v2+1)
        if diff==3:
            e2x=random.randint(v1+2,v2+2)
        pkt+=10
    if p1XY.colliderect(e3XY) or p2XY.colliderect(e3XY) or p3XY.colliderect(e3XY):
        e3XY.y=random.randint(400,560)
        e3XY.x=random.randint(850,950)
        if diff==1:
            e3x=random.randint(v1,v2)
        if diff==2:
            e3x=random.randint(v1+1,v2+1)
        if diff==3:
            e3x=random.randint(v1+2,v2+2)
        pkt+=10
    if p1XY.colliderect(e4XY) or p2XY.colliderect(e4XY) or p3XY.colliderect(e4XY):
        e4XY.y=random.randint(50,560)
        e4XY.x=random.randint(2000,2200)
        if diff==1:
            e4x=4
        if diff==2:
            e4x=5
        if diff==3:
            e4x=6
        pkt+=30

    if p1XY.colliderect(e1XY) or p1XY.colliderect(e2XY) or p1XY.colliderect(e3XY) or p1XY.colliderect(e4XY):
        p1XY.x=825
    if p2XY.colliderect(e1XY) or p2XY.colliderect(e2XY) or p2XY.colliderect(e3XY) or p2XY.colliderect(e4XY):
        p2XY.x=825
    if p3XY.colliderect(e1XY) or p3XY.colliderect(e2XY) or p3XY.colliderect(e3XY) or p3XY.colliderect(e4XY):
        p3XY.x=825
    
    if pkt==420:
        lXY.y=5
    else:
        lXY.y=(-100)

    upXY.x-=upx
    upXY.y-=upy
        
    e1XY.x-=e1x
    e2XY.x-=e2x
    e3XY.x-=e3x
    e4XY.x-=e4x

    p1XY.x+=p1x
    p2XY.x+=p2x
    p3XY.x+=p3x
    
    okienko.fill((50,50,100))

    okienko.blit(statek,sXY)
    okienko.blit(enemy1,e1XY)
    okienko.blit(enemy2,e2XY)
    okienko.blit(enemy3,e3XY)
    okienko.blit(enemy4,e4XY)
    okienko.blit(pocisk1,p1XY)
    okienko.blit(pocisk2,p2XY)
    okienko.blit(pocisk3,p3XY)
    okienko.blit(HP,hpXY)
    okienko.blit(score,scXY)
    okienko.blit(hp1,hp1XY)
    okienko.blit(hp2,hp2XY)
    okienko.blit(hp3,hp3XY)
    okienko.blit(up,upXY)
    okienko.blit(poz1,pz1XY)
    okienko.blit(poz2,pz2XY)
    okienko.blit(poz3,pz3XY)
    okienko.blit(lisc,lXY)
    punktuj()

    
    if hp>=1:
        hp3XY.y=(-100)
    if hp>=2:
        hp2XY.y=(-100)
    else:
        hp2XY.y=(10)
    if hp>=3:
        sy=0
        p1x=0
        p2x=0
        p3x=0
        p1XY.y=700
        p2XY.y=700
        p3XY.y=700
        hp1XY.y=(-100)
        upXY.y=(-100)
        upy=0
        okienko.blit(napis,nXY)

           
    pygame.display.update()
    fps.tick(60)
