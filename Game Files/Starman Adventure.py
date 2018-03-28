import pygame
from pygame.locals import *
import time

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


#Each array is [xpos,ypos,width,height]
platformRects = [[-500,500,2000,250],[325,350,150,30],[600,50,150,30],[50,-250,150,30],[50,-550,150,30],[200,-850,150,30],
                 [650,-1000,150,30],[100,-1330,150,30],[500,-1660,150,30],[50,-1970,150,30],[500,-2275,150,30],[550,-2590,150,30],
                 [750,-2920,50,30],[50,-3250,40,30],[250,-3580,30,30],[450,-3910,30,30],[]]

screen = pygame.display.set_mode((width,height))

player = Player()
players = pygame.sprite.Group()
platforms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

platformList = []

new_platform = Platform(750,350,50,50,"goal")
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

fpsincrease = True

jump = 20

running = True

armWidth= 20

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
        elif playerLeft<=platform.rect.right and playerLeft>=platform.rect.right-10 and playerRight>=platform.rect.right and player.rect.top<=platform.rect.bottom and player.rect.bottom>=platform.rect.top+15:
            player.xvelocity=0
            player.rect.left=platform.rect.right-armWidth
            if platform.variant == "goal":
                running = False
        elif player.rect.bottom>=platform.rect.top-1 and ((platform.rect.height<40 and player.rect.bottom <= platform.rect.bottom)or(player.rect.bottom <= platform.rect.bottom- platform.rect.height*.8)) and playerRight >= platform.rect.left and playerLeft <= platform.rect.right and player.yvelocity>=0:        
            player.yvelocity=0
            player.yscroll=0
            if pressed_keys[K_UP]:
                player.yvelocity=-1*jump
            if platform.variant == "goal":
                running = False
            player.rect.bottom=platform.rect.top-1
        elif player.rect.top<=platform.rect.bottom and player.rect.top>=platform.rect.top and playerRight>=platform.rect.left and playerLeft<=platform.rect.right and player.yvelocity<=0:
            player.yvelocity=0
            player.yscroll=0
            player.rect.top=platform.rect.bottom+1
            if platform.variant == "goal":
                running = False
        
            
    if player.rect.bottom>=height and pressed_keys[K_UP]:
        player.yvelocity=-1*jump
        player.rect.move_ip(0,-1)
                    
    screen.blit(background, (0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
        
    
    test1y = test1.tempy
    test2y= test2.tempy

color = 0
for i in range(2550):
    screen.fill((color,color,color))
    pygame.display.flip()
    color += 0.1    

pygame.quit()
