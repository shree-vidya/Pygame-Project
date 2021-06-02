import pygame
import os
from pygame import mixer
from pygame import time
import random
from PIL import Image
# from Graveyardtileset import CROSSHAIR
from PIL import Image
import math



path = os.getcwd()
path1 = os.path.abspath(os.path.join(path, os.pardir))

GAMEPATH = path1
FILEPATH = os.path.join(path1, "Game Module")
THEMEPATH = os.path.join(path1, "Theme", "Summer")
ENEMYPATH = os.path.join(path1, "Enemy","Left_facing", "1" )
RELATIVE = 0

class Assets():
    def __init__(self):
        # Clock
        self.clock = pygame.time.Clock()
        # Fonts
        self.fonts = {"default" : pygame.font.Font('freesansbold.ttf', 32)}
        # Music
        # self.music = {"default": mixer.Sound()}
        self.background = pygame.image.load(os.path.join(GAMEPATH, "Theme", "Summer", "BG.png"))
        self.bgX = 0
        self.bgX2 = self.background.get_width()
        self.screen = pygame.display.set_mode((self.bgX2, 750))
        pygame.display.set_caption("Level : Summer") 
        

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
        self.isidle = True
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
        self.isidle = False
        if self.walkcount + 1 >= 18:
            self.walkcount = 0
        if direction is "left":
                self.screen.blit(self.characterleft[f'Run__00{self.walkcount//3}'], (x,y))
        elif direction is 'right':
                self.screen.blit(self.characterright[f'Run__00{self.walkcount//3}'], (x,y))

    def idle(self, direction, x, y):
        self.isidle = True
        if self.walkcount + 1 >= 18:
            self.walkcount = 0
        if direction is "left":
                self.screen.blit(self.characterleft[f'Idle__00{self.walkcount//3}'], (x,y))
        elif direction is 'right':
                self.screen.blit(self.characterright[f'Idle__00{self.walkcount//3}'], (x,y))

    def draw(self,win):
        self.hitbox = (self.x , self.y, self.char.get_width(), self.char.get_height())  
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        

    def hit(self):
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        self.screen.blit(text, (600 - (text.get_width()/2),200))
        pygame.display.update()
        pygame.time.delay(500)

    def hit_enemy(self):
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-25', 1, (255,0,0))
        self.screen.blit(text, (600 - (text.get_width()/2),200))
        pygame.display.update()
        pygame.time.delay(500)
        
    def gain(self):
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('+10', 1, (0,153,0))
        self.screen.blit(text, (600 - (text.get_width()/2),200))
        pygame.display.update()
        pygame.time.delay(100)

class Enemy():
    img = pygame.image.load(os.path.join(ENEMYPATH, "RUN_0.png"))
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walkCount = 0
        self.hitbox = [self.x , self.y, self.img.get_width(), self.img.get_height()]
        self.isenemy = True
        self.enemyleft = {
            filename.split(".")[0] : pygame.image.load(os.path.join(GAMEPATH, "Enemy", "Left_facing", "1", filename)) for filename in os.listdir(os.path.join(GAMEPATH, "Enemy", "Left_facing", "1")) if filename.endswith(".png")
        }
        self.enemyright = {
            filename.split(".")[0] : pygame.image.load(os.path.join(GAMEPATH, "Enemy", "Right_facing", "1", filename)) for filename in os.listdir(os.path.join(GAMEPATH, "Enemy", "Right_facing", "1")) if filename.endswith(".png")
        }
    
    def draw(self,win,rect,idle):
        # self.move()
        if self.walkCount + 1 >= 21:
            self.walkCount = 0
        
        if rect[0] > self.x and idle == True:
            self.x += 5
        if rect[0] < self.x and idle == True:
            self.x -=5
          
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        # win.blit(self.img, (self.x,self.y))
        if rect[0] > self.x:
            self.hitbox = (self.x- 28, self.y +25, self.img.get_width() -25, self.img.get_height()-25)
            win.blit(self.enemyright[f'RUN_{self.walkCount//3}'],(self.x,self.y))
            self.walkCount += 1
            # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        else: 
            self.hitbox = (self.x +30, self.y+25, self.img.get_width()-25, self.img.get_height()-25)
            win.blit(self.enemyleft[f'RUN_{self.walkCount//3}'],(self.x,self.y))
            self.walkCount += 1
            # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

        

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class Weapon(object): 
    def __init__(self,y,width,height,char_x):
        self.x = char_x
        self.y = y
        self.i = 0
        self.angle = 0
        self.width = width
        self.height = height
        self.weapons = []
        self.img = pygame.transform.scale(pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Weapon", "Kunai_0.png")),(64,32))
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())
        for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Weapon")):
             if filename.endswith(".png"):
                 self.weapons.append(pygame.transform.scale(pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Weapon", filename)),(64,32)))
        
        
    def draw(self,win,rect):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        if self.i > 71:
            self.i=0
        win.blit(self.weapons[self.i], (self.x,self.y))
        self.i += 1
        # win.blit(self.img, (self.x,self.y))
        
    def get_angle(self,clickx,clicky,rect):
        y = rect[1]+60
        x = rect[0]+40
        try:
            angle = math.atan((y - clicky) / (x - clickx))
        except:
            angle = math.pi / 2

        if clicky < y and clickx > x:
            angle = abs(angle)
        elif clicky < y and clickx < x:
            angle = math.pi - angle 
        elif clicky > y and clickx < x:
            angle = math.pi + abs(angle)
        elif clicky > y and clickx > x:
            angle = (math.pi * 2) - angle

        return angle

    def projectile(self,startx, starty,angle, power, time):
        
        velx = math.cos(angle) * power
        vely = math.sin(angle) * power

        disx = velx * time
        disy = (vely * time) + ((-4.9 * (time)** 2)/2) - 20

        newx = round(disx +startx)
        newy = round(starty - disy)
        
        return (newx, newy)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1] and rect[1] < self.hitbox[1] + self.hitbox[3]:
                return True
        return False

    def gain(self,screen):
        self.screen = screen
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('+25', 1, (0,153,0))
        self.screen.blit(text, (600 - (text.get_width()/2),200))
        pygame.display.update()
        pygame.time.delay(20)
    
class Layout():
    def __init__(self, screen):
        
        self.screen = screen
        self.decorations = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Objects", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Objects"))
        }
        self.tiles = {
             filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }

class Tree(object):  
    
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Tree_3.png"))
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y+30
        self.width = width
        self.height = height
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height()) 
        
    def draw(self,win):
        self.hitbox = (self.x , self.y, self.img.get_width(), self.img.get_height())  
        # pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        win.blit(self.img, (self.x,self.y)) 

    def collide(self, rect):
        return False        

class Bush(object):  
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Bush (3).png"))
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
        self.y = y+30
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


class Mushroom1(object):  
    img = pygame.image.load(os.path.join(THEMEPATH, "Objects", "Mushroom_1.png"))
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

class Summer:
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
        self.vel = 30
        right = True
        left = False
        idle = True
        self.bgX=0
        self.bgX2=self.background.get_width()
        self.obstacles = []
        self.coins = []
        self.enemies = []
        self.shoot = []
        time = 0
        weapon_there = False
        score=0
        obstacle_there = False
        pygame.time.set_timer(pygame.USEREVENT, random.randrange(3000, 6000))
        self.tiles = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }

        # cursor = pygame.cursors.compile(CROSSHAIR, black='X', white='.', xor='o')
        # pygame.mouse.set_cursor((24, 24), (12, 12), *cursor)

        

        while self.play:
            self.asset.clock.tick(30)
            self.character.draw(self.screen)

            self.screen.blit(self.background, (self.bgX,0))
            self.screen.blit(self.background, (self.bgX2,0))
            
            for i in range(1500//128+1):
                self.background.blit(self.tiles['2'], (128*i,750-128))
            
            # font = pygame.font.SysFont("comicsans", 50, True)
            # text = font.render("Score: " + str(score), 1, (255,255,0))
            # self.screen.blit(text, (1000, 10))

            font = pygame.font.Font('freesansbold.ttf',32)
            text = font.render('Score : ' + str(score), True, (0,0,0))
            self.screen.blit(text, (10, 10))

            for obstacle in self.obstacles:
                obstacle_there = True
                obstacle.draw(self.screen)
                if obstacle.collide(self.character.hitbox):
                    self.character.hit()
                    self.obstacles.pop(self.obstacles.index(obstacle))
                    score -= 5
                obstacle_there = False

            for enemy in self.enemies:
                obstacle_there = True
                enemy.draw(self.screen,self.character.hitbox,self.character.isidle)
                if enemy.collide(self.character.hitbox):
                    self.character.hit_enemy()
                    self.enemies.pop(self.enemies.index(enemy))
                    score -= 25
                    obstacle_there = False
                
            for weapon in self.shoot:
                weapon_there = True
                if weapon.y > self.character.y + 100:
                    self.shoot.pop(self.shoot.index(weapon))
                    weapon_there = False
                weapon.draw(self.screen,self.character.hitbox)
                time += 2
                angle = weapon.get_angle(clickx,clicky,self.character.hitbox)
                pos = weapon.projectile(weapon_x,weapon_y,angle,power,time)
                # if(pos[0]<0 or pos[1]<0):
                #     self.shoot.pop(self.shoot.index(weapon))
                #     weapon_there = False
                weapon.x = pos[0]
                weapon.y = pos[1]
                # weapon.x += 50
                # weapon.y -= 50
                 # weapon.y = ((self.character.x + 40) * math.tan(weapon.angle))-((9.8 * ((self.character.x + 40) ** 2))/(2 * (30 ** 2) * (math.cos(weapon.angle)**2)))
                for enemy in self.enemies:
                    if weapon.collide(enemy.hitbox) and weapon_there == True:
                        self.shoot.pop(self.shoot.index(weapon))
                        weapon_there = False
                        weapon.gain(self.asset.getscreen())
                        self.enemies.pop(self.enemies.index(enemy))
                        obstacle_there = False
                        score += 25
                

            for coin in self.coins:
                obstacle_there = True
                coin.draw(self.screen)
                if coin.collide(self.character.hitbox):
                    self.character.gain()
                    self.coins.pop(self.coins.index(coin))
                    score += 10
                obstacle_there = False

            self.charcontroller(right, left, idle)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
                if event.type == pygame.USEREVENT and obstacle_there == False:
                    r = random.randrange(0,15)
                    if r == 0:
                        self.obstacles.append(Bush(self.background.get_width(), 497+80, 48, 310))
                    elif r == 1:
                        self.obstacles.append(Crate(self.background.get_width(), 497+25, 48, 310))
                    elif r == 2:
                        self.obstacles.append(Stones(self.background.get_width(), 497+80, 48, 310))
                    elif r == 3 or r == 12:
                        self.obstacles.append(Crate(self.background.get_width(), 497+25, 48, 310))
                    elif r == 4 or r == 6 or r == 7 or r == 8:
                        self.coins.append(Coins(self.background.get_width(), 497+65, 48, 310))
                    elif r == 5 or r == 9 or r == 10 or r == 11:
                        self.obstacles.append(Tree(self.background.get_width(), 497-175, 150, 310))
                    else:
                        self.enemies.append(Enemy(self.background.get_width(), 505, 64, 64))       
   
   
            keys=pygame.key.get_pressed()
            if keys[pygame.K_q or pygame.K_ESCAPE]:
                self.play = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and  weapon_there == False and len(self.enemies) > 0:
                    self.shoot.append(Weapon(self.character.y + 60, 16, 16, self.character.x + 40))
                    clickx ,clicky = pygame.mouse.get_pos()
                    weapon_x = self.character.x + 40
                    weapon_y = self.character.y + 60
                    line = [(weapon_x, weapon_y),(clickx,clicky)]
                    power = math.sqrt((line[1][1] - line[0][1])**2 + (line[1][0] - line[0][0])**2 )/7
                    time = 0
                
                    


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
                    self.bgX += 25
                    self.bgX2 += 25

                    if  self.bgX >=  self.background.get_width():  
                        self.bgX =  self.background.get_width() * -1
                    
                    if  self.bgX2 >=  self.background.get_width():
                        self.bgX2 =  self.background.get_width() * -1
                    for obstacle in self.obstacles: 
                        obstacle.x += 25
                        if obstacle.x < obstacle.width * -1: 
                            self.obstacles.pop(self.obstacles.index(obstacle))
                    for enemy in self.enemies: 
                        enemy.x += 5
                        # enemy.end -= 7
                        # enemy.hitbox[0] += 7
                        if enemy.x < enemy.width * -1: 
                            self.enemies.pop(self.enemies.index(enemy))
                            obstacle_there = False
                    for coin in self.coins: 
                        coin.x += 25
                        if coin.x < coin.width * -1: 
                            self.coins.pop(self.coins.index(coin))

            elif keys[pygame.K_RIGHT] and self.character.x < self.background.get_width() - self.character.width - self.vel:
                self.character.walkcount += 1
                if self.character.walkcount == 20:
                    self.character.walkcount = 0
                left = False
                right = True
                idle = False
                if self.character.x < (self.background.get_width()/2)-self.character.width:
                    self.character.x += self.vel
                else:
                    self.bgX -= 25
                    self.bgX2 -= 25

                    if  self.bgX <=  self.background.get_width() * -1:  
                        self.bgX =  self.background.get_width()
                    
                    if  self.bgX2 <=  self.background.get_width() * -1:
                        self.bgX2 =  self.background.get_width()
                    for obstacle in self.obstacles: 
                        obstacle.x -= 25
                        if obstacle.x < obstacle.width * -1: 
                            self.obstacles.pop(self.obstacles.index(obstacle))
                    for coin in self.coins: 
                        coin.x -= 25
                        if coin.x < coin.width * -1: 
                            self.coins.pop(self.coins.index(coin))
                    for enemy in self.enemies: 
                        enemy.x -= 27
                        if enemy.x < self.character.x - 120:
                            enemy.x +=27
                        # enemy.end -= 7
                        # enemy.hitbox[0] -= 7
                        if enemy.x < enemy.width * -1: 
                            self.enemies.pop(self.enemies.index(enemy))
                            obstacle_there = False
                           
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
    g = Summer()
    g.game()
