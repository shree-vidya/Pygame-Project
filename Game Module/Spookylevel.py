import pygame
import os
from pygame import mixer

GAMEPATH = os.getcwd()
FILEPATH = os.path.join(GAMEPATH, "Game Module")
THEMEPATH = os.path.join(GAMEPATH, "Theme", "Graveyard")
RELATIVE = 0

class Assets():
    def __init__(self):
        # Clock
        self.clock = pygame.time.Clock()
        # Fonts
        self.fonts = {"default" : pygame.font.Font('freesansbold.ttf', 32)}
        # Music
        # self.music = {"default": mixer.Sound()}
        self.screen = pygame.display.set_mode((1500, 750))
        pygame.display.set_caption("Level 3: Graveyard") 
        self.background = pygame.image.load(os.path.join(GAMEPATH, "Theme", "Graveyard", "BG.png"))

    def getscreen(self):
        return self.screen


class Character:
    def __init__(self, screen):
        self.screen = screen

        self.x = 0
        self.y = 750-128-125
        self.walkcount = 0

        self.characterleft = {}
        self.characterright = {}

        for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Left_facing")):
            if filename.endswith(".png"):
                self.characterleft[filename.split(".")[0]] = pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Left_facing", filename))
        
        for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Right_facing")):
            if filename.endswith(".png"):
                self.characterright[filename.split(".")[0]] = pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Right_facing", filename))

    def walk(self, direction, x, y):
        if direction is "left":
            self.screen.blit(self.characterleft[f'Run__00{self.walkcount//2}'], (x,y))
        elif direction is 'right':
            self.screen.blit(self.characterright[f'Run__00{self.walkcount//2}'], (x,y))

    def idle(self, direction, x, y):
        if direction is "left":
            self.screen.blit(self.characterleft[f'Idle__00{self.walkcount//3}'], (x,y))
        elif direction is 'right':
            self.screen.blit(self.characterright[f'Idle__00{self.walkcount//3}'], (x,y))

class Enemy:
    pass

class Layout():
    def __init__(self, screen):
        self.screen = screen
        self.decorations = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Objects", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Objects"))
        }
        self.tiles = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }

    def loadfloors(self):
        for i in range(1500//128 + 1):
            self.screen.blit(self.tiles['Tile (2)'], (128*i,750-128))

class Graveyard:
    def __init__(self):
        pygame.init()
        self.asset = Assets()
        param = self.asset.getscreen()
        self.layout = Layout(param)
        self.character = Character(param)

    def setup(self):
        self.screen = pygame.display.set_mode((1500, 750))
        pygame.display.set_caption("Level 3: Graveyard") 
        self.background = self.asset.background
    
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

        while self.play:
            self.asset.clock.tick(40)

            self.screen.fill((0,0,0))
            self.screen.blit(self.background, (0,0))
            self.layout.loadfloors()
            self.charcontroller(right, left, idle)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    self.play = False
                    break
                if event.key == pygame.K_LEFT:
                    self.character.walkcount += 1
                    if self.character.walkcount == 20:
                        self.character.walkcount = 0
                    self.character.x -= self.vel
                    left = True
                    right = False
                    idle = False
                if event.key == pygame.K_RIGHT:
                    self.character.walkcount += 1
                    if self.character.walkcount == 20:
                        self.character.walkcount = 0
                    self.character.x += self.vel
                    left = False
                    right = True
                    idle = False
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    left = True
                    right = False
                    idle = True
                if event.key == pygame.K_RIGHT:
                    left = False
                    right = True
                    idle = True
            pygame.display.update()
        
if __name__ == "__main__":
    g = Graveyard()
    g.game()
