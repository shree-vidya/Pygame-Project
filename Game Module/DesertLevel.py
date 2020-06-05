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
        self.hitbox = (self.x , self.y, self.width, self.height)

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

    def draw(self,win):
        self.hitbox = (self.x , self.y, self.char.get_width(), self.char.get_height())  
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        

    def hit(self):
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        self.screen.blit(text, (600 - (text.get_width()/2),200))
        pygame.display.update()
        pygame.time.delay(500)
        
    def gain(self):
        print("gain")
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('+10', 1, (0,153,0))
        self.screen.blit(text, (600 - (text.get_width()/2),200))
        pygame.display.update()
        pygame.time.delay(100)

class Layout():
    def __init__(self, screen):
        
        self.screen = screen
        self.decorations = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Objects", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Objects"))
        }
        self.tiles = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }
            

class Cacti(object):  
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Cactus (1).png"))
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())

    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class Crate(object):  
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Crate.png"))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height()) 
        
    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class Stones(object):  
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Stone.png"))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height()) 
        
    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class Skeletons(object):  
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Skeleton.png"))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())
        
    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class Coins(object):  
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "002-money.png"))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())
        
    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

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
        self.obstacles = []
        self.coins = []
        score=0
        pygame.time.set_timer(pygame.USEREVENT, random.randrange(3000, 6000))
        self.tiles = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }
        

        while self.play:
            self.asset.clock.tick(30)
            self.character.draw(self.screen)

            self.screen.blit(self.background, (self.bgX,0))
            self.screen.blit(self.background, (self.bgX2,0))
            
            for i in range(1500//128+1):
                self.background.blit(self.tiles['2'], (128*i,750-128))
            
            font = pygame.font.SysFont("comicsans", 50, True)
            text = font.render("Score: " + str(score), 1, (0,0,0))
            self.screen.blit(text, (1000, 10))

            for obstacle in self.obstacles:
                obstacle.draw(self.screen)
                if obstacle.collide(self.character.hitbox):
                    self.character.hit()
                    self.obstacles.pop(self.obstacles.index(obstacle))
                    score -= 5

            for coin in self.coins:
                coin.draw(self.screen)
                if coin.collide(self.character.hitbox):
                    self.character.gain()
                    self.coins.pop(self.coins.index(coin))
                    score += 10

            self.charcontroller(right, left, idle)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
                if event.type == pygame.USEREVENT:
                    r = random.randrange(0,5)
                    if r == 0:
                        self.obstacles.append(Cacti(self.background.get_width(), 497+20, 64, 64))
                    elif r == 1:
                        self.obstacles.append(Crate(self.background.get_width(), 497+25, 48, 310))
                    elif r == 2:
                        self.obstacles.append(Stones(self.background.get_width(), 497+55, 48, 310))
                    elif r == 3:
                        self.obstacles.append(Skeletons(self.background.get_width(), 497+75, 48, 310))
                    elif r == 4:
                        self.coins.append(Coins(self.background.get_width(), 497+65, 48, 310))
   
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
                    for obstacle in self.obstacles: 
                        obstacle.x += 15
                        if obstacle.x < obstacle.width * -1: 
                            self.obstacles.pop(self.obstacles.index(obstacle))
                    for coin in self.coins: 
                        coin.x += 15
                        if coin.x < coin.width * -1: 
                            self.coins.pop(self.coins.index(coin))

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
                    for obstacle in self.obstacles: 
                        obstacle.x -= 15
                        if obstacle.x < obstacle.width * -1: 
                            self.obstacles.pop(self.obstacles.index(obstacle))
                    for coin in self.coins: 
                        coin.x -= 15
                        if coin.x < coin.width * -1: 
                            self.coins.pop(self.coins.index(coin))
                           
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
