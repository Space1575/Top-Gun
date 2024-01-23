import pygame
import random
import time
import math
import sys
import os
pygame.font.init()

pygame.init()


W = 600
H = 650
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption("Top Gun")

Height = 80
Width = 80
WIN = False

FPS = 90

PlaneX = 200
PlaneY = H - 90
"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)"""

falling_piece_count = 0
F = pygame.font.SysFont('comicsans',40)

FONT = pygame.font.SysFont('comicsans',30)
#--------
T = ""
level = 1
Health = 20

#sky backgr images
sky1 =  pygame.image.load(os.path.join('Assets','sky.jpg'))
sky1_1 = pygame.transform.scale(sky1,(W,H))#sky backg 1
skyx,skyy = 0,0

hit = False
scroll = 0

gameover1 = pygame.image.load(os.path.join('Assets','123.png')).convert_alpha()
gameover = pygame.transform.scale(gameover1,(450,100))


win = pygame.image.load(os.path.join('Assets','win.png'))

#--------------------------------
#-------------------------------------------------------------------
plane_x,plane_y = PlaneX,PlaneY
#Player images
Player2 = pygame.image.load(os.path.join('Assets', 'jet 2.png'))
JET_1 = pygame.transform.scale(Player2, (Width,Height)).convert_alpha()#level 1

Jet = pygame.image.load(os.path.join('Assets', 'JET 3.png'))
jet_2 = pygame.transform.scale(Jet,(Width,Height))#level 2

JET = pygame.image.load(os.path.join('Assets', 'JET 6.png'))
Jet_3 = pygame.transform.scale(JET,(80,70))#level3

Jet4 = pygame.image.load(os.path.join('Assets','JET 4.png'))
jet_4 = pygame.transform.scale(Jet4,(Width,Height)).convert_alpha()#level 4

if level == 1:
    player = JET_1
elif level == 2:
    player = jet_2
elif level == 3:
    player = Jet_3
elif level == 4:
    player = jet_4

box = pygame.Rect(PlaneX+15,PlaneY+2,Width-30,Height-15)
move = 2#moving
Border = pygame.Rect(0,H-10,W,10)
sky = sky1_1 #making sky background
sky_width = sky.get_height()
tile = H / sky_width
obstacle = pygame.Rect(0,0,W,70)




bullet = pygame.Rect(box.x,box.y,2,5)
bullet.x,bullet.y = box.x,box.y
#-------------------------------------------------------------
def Player_costume(escalape,):
    global player,move,level,S,WIN
    if round(escalape) >=6 and round(escalape) < 60:
        Text("Level 1",F)
        S =random.randint(2,6)
        level = 1
        player = JET_1
        move = 2
        return player

    if round(escalape) >=60 and round(escalape) < 120:
            Text("Level 2",F)
            S =random.randint(8,12)
            level = 2
            player = jet_2
            move = 3
            return player
    elif round(escalape) >=120 and round(escalape) < 190:
        level = 3
        Text("Level 3",F)
        S = random.randint(6,15)
        player = Jet_3
        return player
    elif round(escalape) >=190 and round(escalape) < 250:
        level = 4
        Text("Level 4",F)
        S = random.randint(10,20)
        player = jet_4
        return player
    elif round(escalape) >= 250 and round(escalape) < 255:
        level = 5
        screen.blit(win,(W//2,H//2))
    elif round(escalape) >=255 and round(escalape) < 258:
        Text("You won!!",FONT)
        level = 6    
    elif level == 6:
        WIN = True
#----------------------------------------------
def Movement():
    global plane_x,plane_y
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT or pygame.K_a] and plane_x > 0 - 17:#moving
        plane_x -= move
        box.x -= move 
    if key[pygame.K_RIGHT or pygame.K_d] and plane_x < 536:
        plane_x += move
        box.x += move
    if key[pygame.K_UP ] and plane_y > obstacle.y + 70:
        plane_y -= move
        box.y -= move
    if key[pygame.K_DOWN or pygame.K_s] and plane_y < Border.y -60:
        plane_y += move
        box.y += move

    return  plane_x,plane_y


def drawing(box,T,escalape,obj):
    screen.fill((0,180,230))

    screen.blit(sky,(0,0))
    
    if Health <= 0:
        screen.blit(gameover,(200,400))
    pygame.draw.rect(screen,(0,0,0),Border)
    pygame.draw.rect(screen,(0,0,0),obstacle,5)

    for objec in obj:
        pygame.draw.rect(screen,(196, 164, 132),objec)
    img2 = FONT.render(f"HP:{round(Health)}", 1, (0,0,0))
    screen.blit(img2,(480,10))

    plane_x,plane_y = Movement()

    TEXT_TIME = FONT.render(f"Time: {round(escalape)}s",1,"black")
    screen.blit(TEXT_TIME,(2,10))
    screen.blit(player,(plane_x,plane_y))

    if escalape > 0 and escalape <= 2:
            Text1 ("Welcome to the Top  Gun",F)
    elif escalape > 2 and escalape <= 4:
            Text1("Use arrows keys to move. ",F)
    elif escalape >4 and escalape <= 5:
            Text1("",F)


def Text(T,F,):
    img = F.render(T, 1, (0,0,0))
    screen.blit(img,(W/2 - 70,8))


def Text1(Tex,F,):
    img1 = F.render(Tex, 1, (0,0,0))
    screen.blit(img1,(20,100))
obj = []

def main():  #main game loop
    global run,clock,Health
    falling_piece_count = 2000000
    start_time = time.time()
    escalape = 0

    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((W,H))
    pygame.display.set_caption("Top Gun")
    hit = False
    run = True
    while run: 
        escalape=time.time()-start_time
        falling_piece_count += clock.tick(FPS)
        pause = random.randint(1000,2000)

        if escalape >= 6 and WIN != True:
            if falling_piece_count > pause:
                for _ in range(S):
                    object_y = -20
                    object_x = random.randint(0,W-20)
                    objec = pygame.Rect(object_x,object_y,20,20)
                    obj.append(objec)

                    pause = random.randint(10,20)
                    falling_piece_count = 0


        for event in pygame.event.get():#exit from the pygame
            if event.type == pygame.QUIT:
                run = False
                pygame.quit() 
                sys.exit()
        for objec in obj[:]:
            objec.y += 2.4
            if objec.y >= H - 30:
                obj.remove(objec)
            if objec.colliderect(box):
                Health -= 1
                obj.remove(objec)

        if Health <= 0:
            Health = 0

            screen.blit(gameover,(80,100 ))
            pygame.display.update()
            hit = True
        
        if WIN:
            screen.blit()

        if hit:
            pygame.time.delay(2000)
            break
                
        drawing(box,T,escalape,obj)
        Player_costume(escalape)
        
        pygame.display.update()        
#screen update



#-------------------------------------------------------
main()
