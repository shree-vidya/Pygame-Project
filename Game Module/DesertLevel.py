import pygame
import os
from pygame import mixer
from pygame import time
import random


GAMEPATH = os.getcwd()
FILEPATH = os.path.join(GAMEPATH, "Game Module")
THEMEPATH = os.path.join(GAMEPATH, "Theme", "Desert")
RELATIVE = 0

class Assets():
    def __init__(self):
        # Clock
        self.clock = pygame.time.Clock()
        # Fonts
        self.fonts = {"default" : pygame.font.Font('freesansbold.ttf', 32)}
        # Music
        # self.music = {"default": mixer.Sound()}
        self.background = pygame.image.load(os.path.join(GAMEPATH, "Theme", "Desert", "BG.png"))
        self.bgX = 0
        self.bgX2 = self.background.get_width()
        self.screen = pygame.display.set_mode((self.bgX2, 750))
        pygame.display.set_caption("Level 1: Desert") 
        

    def getscreen(self):
        return self.screen


class Character:
    def __init__(self, screen):
        self.screen = screen
        self.char=pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Right_facing", "Idle__000.png"))
        self.width=self.char.get_width()
        self.height=self.char.get_height()
        self.x = 0
        self.y = 750-128-125
        self.walkcount = 0
        self.idlecount = 0
        self.isJump=False
        self.jumpcount=10

        self.characterleft = {
            filename.split(".")[0] : pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Left_facing", filename)) for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Left_facing")) if filename.endswith(".png")
        }
        self.characterright = {
            filename.split(".")[0] : pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Right_facing", filename)) for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Right_facing")) if filename.endswith(".png")
        }

    def walk(self, direction, x, y):
        if direction is "left":
            self.screen.blit(self.characterleft[f'Run__00{self.walkcount//3}'], (x,y))
        elif direction is 'right':
            self.screen.blit(self.characterright[f'Run__00{self.walkcount//3}'], (x,y))

    def idle(self, direction, x, y):
        if direction is "left":
            self.screen.blit(self.characterleft[f'Idle__00{self.walkcount//3}'], (x,y))
        elif direction is 'right':
            self.screen.blit(self.characterright[f'Idle__00{self.walkcount//3}'], (x,y))

class Layout():
    def __init__(self, screen):
        
        self.screen = screen
        self.decorations = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Objects", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Objects"))
        }
        self.tiles = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }
        
    # def loadfloors(self):
    #     for i in range(1500//128+1):
    #         self.asset.background.blit(self.tiles['2'], (128*i,750-128))
            

class Cacti(object):  
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Cactus (1).png"))

    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

class Crate(object):  
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Crate.png"))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

class Stones(object):  
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Stone.png"))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

class Skeletons(object):  
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Skeleton.png"))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

class Desert:
    def __init__(self):
        pygame.init()
        self.asset = Assets()
        param = self.asset.getscreen()
        self.layout = Layout(param)
        self.character = Character(param)
        self.bgX=self.asset.bgX
        self.bgX2=self.asset.bgX2

    def setup(self):
        self.background = self.asset.background
        self.screen = pygame.display.set_mode((self.bgX2, 750))
        
    
    def charcontroller(self, r, l, i):
        if i:
            if r:
                self.character.idle("right", self.character.x, self.character.y)
            elif l:
                self.character.idle("left", self.character.x, self.character.y)
        else:
            if r:
                self.character.walk("right", self.character.x, self.character.y)
            elif l:
                self.character.walk("left", self.character.x, self.character.y)

    def game(self):
        self.setup()
        self.play = True
        self.vel = 15
        right = True
        left = False
        idle = True
        self.bgX=0
        self.bgX2=self.background.get_width()
        obstacles = []
        pygame.time.set_timer(pygame.USEREVENT, random.randrange(3000, 5000))
        self.tiles = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }
        self.tileX=0
        self.tileX2=self.tiles['2'].get_width()

        while self.play:
            self.asset.clock.tick(30)

            self.screen.blit(self.background, (self.bgX,0))
            self.screen.blit(self.background, (self.bgX2,0))
            
            for i in range(1500//128+1):
                self.background.blit(self.tiles['2'], (128*i,750-128))
            
            for obstacle in obstacles:
                obstacle.draw(self.screen)

            self.charcontroller(right, left, idle)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
                if event.type == pygame.USEREVENT:
                    r = random.randrange(0,4)
                    if r == 0:
                        obstacles.append(Cacti(self.background.get_width(), 497+20, 64, 64))
                    elif r == 1:
                        obstacles.append(Crate(self.background.get_width(), 497+25, 48, 310))
                    elif r == 2:
                        obstacles.append(Stones(self.background.get_width(), 497+55, 48, 310))
                    elif r == 3:
                        obstacles.append(Skeletons(self.background.get_width(), 497+75, 48, 310))
            
            keys=pygame.key.get_pressed()
            if keys[pygame.K_q] or keys[pygame.K_ESCAPE]:
                self.play = False
                break
            if keys[pygame.K_LEFT] and self.character.x > self.vel:
                self.character.walkcount += 1
                if self.character.walkcount == 30:
                    self.character.walkcount = 0
                left = True
                right = False
                idle = False
                if self.character.x < (self.background.get_width()/2)-self.character.width:
                    self.character.x -= self.vel
                else:
                    self.bgX += 15 
                    self.bgX2 += 15

                    if  self.bgX >=  self.background.get_width():  
                        self.bgX =  self.background.get_width() * -1
                    
                    if  self.bgX2 >=  self.background.get_width():
                        self.bgX2 =  self.background.get_width() * -1
                    for obstacle in obstacles: 
                        obstacle.x += 15
                        if obstacle.x < obstacle.width * -1: 
                            obstacles.pop(obstacles.index(obstacle))
            elif keys[pygame.K_RIGHT] and self.character.x < self.background.get_width() - self.character.width - self.vel:
                self.character.walkcount += 1
                if self.character.walkcount == 30:
                    self.character.walkcount = 0
                left = False
                right = True
                idle = False
                if self.character.x < (self.background.get_width()/2)-self.character.width:
                    self.character.x += self.vel
                else:
                    self.bgX -= 15 
                    self.bgX2 -= 15

                    if  self.bgX <=  self.background.get_width() * -1:  
                        self.bgX =  self.background.get_width()
                    
                    if  self.bgX2 <=  self.background.get_width() * -1:
                        self.bgX2 =  self.background.get_width()
                    for obstacle in obstacles: 
                        obstacle.x -= 15
                        if obstacle.x < obstacle.width * -1: 
                            obstacles.pop(obstacles.index(obstacle))
                           
            else:
                idle=True
                self.character.walkCount = 0
            if not(self.character.isJump):
                if keys[pygame.K_UP]:
                    self.character.isJump=True
                    self.character.walkCount = 0
            else:
                if self.character.jumpcount>=-10:
                    neg=1
                    if self.character.jumpcount<0:
                        neg=-1
                    self.character.y-=(self.character.jumpcount**2)*0.5*neg
                    self.character.jumpcount-=1
                else:
                    self.character.isJump=False
                    self.character.jumpcount=10
            if idle:
                self.character.idlecount += 1
                if self.character.idlecount == 30:
                    self.character.idlecount = 0
            pygame.display.update()
        
if __name__ == "__main__":
    g = Desert()
    g.game()
