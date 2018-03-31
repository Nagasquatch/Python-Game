import pygame
from pygame.locals import *
import time
import random

pygame.init()

width = 800
height = 800

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf = pygame.image.load("star.png").convert()
        self.surf=pygame.transform.scale(self.surf,(118,109))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.top = 300
        self.xvelocity = 0
        self.yvelocity = 0
        self.yscroll = 0

    def update(self, pressed_keys):

        if pressed_keys[K_LEFT]:
            self.xvelocity=-5
        if pressed_keys[K_RIGHT]:
            self.xvelocity=5
        
        if self.rect.right < 0:
            self.rect.left = width
        elif self.rect.left > width:
            self.rect.right = 0
            
        if self.rect.top <= 200 and self.yvelocity < 0:
            self.rect.top = 200
            self.yscroll = -1*self.yvelocity
        elif self.rect.bottom >= height-200 and self.yvelocity > 0:
            self.rect.bottom = height-200
            self.yscroll = -1*self.yvelocity
        else:
            self.rect.move_ip(0 , self.yvelocity)
        
        self.rect.move_ip(self.xvelocity, 0)
        self.xvelocity *= 0.5
        if self.xvelocity < 1:
            self.xvelocity = 0
        self.yvelocity += 0.6


class Platform(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos, width, height, variant):
        super(Platform, self).__init__()
        self.surf = pygame.image.load("platform.png").convert()
        self.surf=pygame.transform.scale(self.surf,(width,height))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left = xpos
        self.rect.top = ypos
        self.tempy = ypos
        self.variant = variant
    def update(self):
        self.tempy += player.yscroll
        if self.tempy >1:
            self.rect.y=self.tempy
        else:
            self.rect.y = -1000

zigzag1 = random.randint(0,2)
zigzag2 = random.randint(0,2)
zigzag3 = random.randint(0,2)
zigzag4 = random.randint(0,2)
zigzag5 = random.randint(0,2)
zigzag6 = random.randint(0,2)
zigzag7 = random.randint(0,2)
zigzag8 = random.randint(0,2)
zigzag9 = random.randint(0,2)
zigzag10 = random.randint(0,2)

platx1 = 0
if zigzag1 == 1:
    platx1 = 450
elif zigzag1 == 2:
    platx1 = 650
elif zigzag1 == 0:
    platx1 = 250
platx2 = 0
if zigzag2 == 1:
    platx2 = 450
elif zigzag2 == 2:
    platx2 = 650
elif zigzag2 == 0:
    platx2 = 250
if abs(zigzag1-zigzag2)>1:
    platx2 = 450

platx3 = 0
if zigzag3 == 1:
    platx3 = 450
elif zigzag3 == 2:
    platx3 = 650
elif zigzag3 == 0:
    platx3 = 250
if abs(zigzag2-zigzag3)>1:
    platx3 = 450

platx4 = 0
if zigzag4 == 1:
    platx4 = 450
elif zigzag4 == 2:
    platx4 = 650
elif zigzag4 == 0:
    platx4 = 250
if abs(zigzag3-zigzag4)>1:
    platx4 = 450

platx5 = 0
if zigzag5 == 1:
    platx5 = 450
elif zigzag5 == 2:
    platx5 = 650
elif zigzag5 == 0:
    platx5 = 250
if abs(zigzag4-zigzag5)>1:
    platx5 = 450

platx6 = 0
if zigzag6 == 1:
    platx6 = 450
elif zigzag6 == 2:
    platx6 = 650
elif zigzag6 == 0:
    platx6 = 250
if abs(zigzag5-zigzag6)>1:
    platx6 = 450

platx7 = 0
if zigzag7 == 1:
    platx7 = 450
elif zigzag7 == 2:
    platx7 = 650
elif zigzag7 == 0:
    platx7 = 250
if abs(zigzag6-zigzag7)>1:
    platx7 = 450

platx8 = 0
if zigzag8 == 1:
    platx8 = 450
elif zigzag8 == 2:
    platx8 = 650
elif zigzag8 == 0:
    platx8 = 250
if abs(zigzag7-zigzag8)>1:
    platx8 = 450

platx9 = 0
if zigzag9 == 1:
    platx9 = 450
elif zigzag9 == 2:
    platx9 = 650
elif zigzag9 == 0:
    platx9 = 250
if abs(zigzag8-zigzag9)>1:
    platx9 = 450

platx10 = 0
if zigzag10 == 1:
    platx10 = 450
elif zigzag10 == 2:
    platx10 = 650
elif zigzag10 == 0:
    platx10 = 250
if abs(zigzag9-zigzag10)>1:
    platx10 = 450
    
#Each array is [xpos,ypos,width,height]
platformRects = [[-500,500,2000,250],[325,350,150,30],[600,50,150,30],[50,-250,150,30],[50,-550,150,30],[200,-850,150,30],
                 [650,-1000,150,30],[100,-1330,150,30],[500,-1660,150,30],[50,-1970,150,30],[500,-2275,150,30],[550,-2590,150,30],
                 [750,-2920,50,30],[50,-3250,40,30],[250,-3580,30,30],[450,-3910,30,30],[platx1,-4240,30,30],[platx2,-4570,30,30],
                 [platx3,-4900,30,30],[platx4,-5230,30,30],[platx5,-5560,30,30],[platx6,-5890,30,30],[platx7,-6220,30,30],
                 [platx8,-6550,30,30],[platx9,-6880,30,30],[platx10,-7210,30,30]]

screen = pygame.display.set_mode((width,height))

player = Player()
players = pygame.sprite.Group()
platforms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

platformList = []

new_platform = Platform(440,-7540,50,50,"goal")
platforms.add(new_platform)
all_sprites.add(new_platform)
platformList.append(new_platform)

for plat in platformRects:
    new_platform = Platform(plat[0],plat[1],plat[2],plat[3],"normal")
    platforms.add(new_platform)
    all_sprites.add(new_platform)
    platformList.append(new_platform)

background = pygame.Surface(screen.get_size())
background.fill((20,20,20))

display_width = width
display_height = height

clock = pygame.time.Clock()
FPS = 60
surf = pygame.Surface((75, 75))

surf.fill((255, 255, 255))
rect = surf.get_rect()

pygame.time.set_timer(USEREVENT+1, 1000)

countdown = 25

fpsincrease = True

jump = 20

running = True

armWidth= 20

dead = False

test1=platformList[3]
test2=platformList[4]
test1y = test1.rect.y
test2y= test2.rect.y
while running:
    pressed_keys = pygame.key.get_pressed()
    clock.tick(FPS)
    #polling for game events
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            Player()
            if event.key == K_ESCAPE:
                running = False
                print("Escape")
        elif event.type == QUIT:
            running = False
            print("Quit")
        if event.type == USEREVENT+1:
            print (countdown)
            countdown-=1
            if countdown < 0:
                color = 255
                for i in range(510):
                    screen.fill((color,color,color))
                    pygame.display.flip()
                    color -= 0.5
                running = False
                dead = True
                print("Too slow! To make it out, you'll need pinpoint precision!")
        if event.type == QUIT:
            break
    onCloud = False
    platforms.update()
    player.update(pressed_keys)

    playerRight=player.rect.right-armWidth
    playerLeft=player.rect.left+armWidth
    for platform in platforms:
        
        if playerRight>=platform.rect.left and playerRight<=platform.rect.left+10 and playerLeft<=platform.rect.left and player.rect.top<=platform.rect.bottom and player.rect.bottom>=platform.rect.top+15:
            player.xvelocity=0
            player.rect.right=platform.rect.left+armWidth
            if platform.variant == "goal":
                running = False
                print("You got out with " + str(countdown) + " seconds remaining!")
        elif playerLeft<=platform.rect.right and playerLeft>=platform.rect.right-10 and playerRight>=platform.rect.right and player.rect.top<=platform.rect.bottom and player.rect.bottom>=platform.rect.top+15:
            player.xvelocity=0
            player.rect.left=platform.rect.right-armWidth
            if platform.variant == "goal":
                running = False
                print("You got out with " + str(countdown) + " seconds remaining!")
        elif player.rect.bottom>=platform.rect.top-1 and ((platform.rect.height<40 and player.rect.bottom <= platform.rect.bottom)or(player.rect.bottom <= platform.rect.bottom- platform.rect.height*.8)) and playerRight >= platform.rect.left and playerLeft <= platform.rect.right and player.yvelocity>=0:        
            player.yvelocity=0
            player.yscroll=0
            if pressed_keys[K_UP]:
                player.yvelocity=-1*jump
            if platform.variant == "goal":
                running = False
                print("You got out with " + str(countdown) + " seconds remaining!")
            player.rect.bottom=platform.rect.top-1
        elif player.rect.top<=platform.rect.bottom and player.rect.top>=platform.rect.top and playerRight>=platform.rect.left and playerLeft<=platform.rect.right and player.yvelocity<=0:
            player.yvelocity=0
            player.yscroll=0
            player.rect.top=platform.rect.bottom+1
            if platform.variant == "goal":
                running = False
                print("You got out with " + str(countdown) + " seconds remaining!")
        
    if player.rect.bottom>=height and pressed_keys[K_UP]:
        player.yvelocity=-1*jump
        player.rect.move_ip(0,-1)

    screen.blit(background, (0, 0))
    if dead == False:
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
    
pygame.quit()
