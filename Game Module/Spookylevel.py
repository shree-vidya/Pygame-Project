import pygame
import os
from pygame import mixer

from Graveyardtileset import TILES

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
        self.idlecount = 0

        self.characterleft = {
            filename.split(".")[0] : pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Left_facing", filename)) for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Left_facing")) if filename.endswith(".png")
        }
        self.characterright = {
            filename.split(".")[0] : pygame.image.load(os.path.join(GAMEPATH, "Main_character", "Right_facing", filename)) for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Right_facing")) if filename.endswith(".png")
        }

    def walk(self, direction, x, y):
        if direction is "left":
            self.screen.blit(self.characterleft[f'Run__00{self.walkcount}'], (x,y))
        elif direction is 'right':
            self.screen.blit(self.characterright[f'Run__00{self.walkcount}'], (x,y))

    def idle(self, direction, x, y):
        if direction is "left":
            self.screen.blit(self.characterleft[f'Idle__00{self.walkcount}'], (x,y))
        elif direction is 'right':
            self.screen.blit(self.characterright[f'Idle__00{self.walkcount}'], (x,y))

class Enemy:
    pass

class Layout():
    def __init__(self, screen):
        self.screen = screen
        self.tilesets = TILES
        self.decorations = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Objects", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Objects"))
        }
        self.tiles = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }

    def loadfloors(self):
        global RELATIVE
        # for i in range(1500//128 + 1):
        #     x = 128 * i + RELATIVE
        #     if x > 0:
        #         x = 128 * i - RELATIVE
        #         self.screen.blit(self.tiles['Tile (2)'], (x, 750-128))
        #     else:
        #         RELATIVE = 0
        #         x = 128 * i + RELATIVE
        #         self.screen.blit(self.tiles['Tile (2)'], (x, 750-128))
        for i in self.tilesets.keys():
            for j in self.tilesets[i].keys():
                x, y = self.tilesets[i][j]['hitbox']
                test = x + RELATIVE
                if test > 0:
                    x -= RELATIVE
                else: 
                    RELATIVE = 0
                    x += RELATIVE
                self.screen.blit(self.tilesets[i][j]['Resource'], (x, y))

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
    
    def charcontroller(self, phase):
        if phase is "idleright":
            self.character.idle("right", self.character.x, self.character.y)
        elif phase is "idleleft":
            self.character.idle("left", self.character.x, self.character.y)
        elif phase is "walkright":
            self.character.walk("right", self.character.x, self.character.y)
        elif phase is "walkleft":
            self.character.walk("left", self.character.x, self.character.y)

    def game(self):
        global RELATIVE
        self.setup()
        self.play = True
        self.vel = 20
        phase = "idleleft"

        while self.play:
            self.asset.clock.tick(30)

            self.screen.fill((0,0,0))
            self.screen.blit(self.background, (0,0))
            
            self.charcontroller(phase)
            self.layout.loadfloors()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    self.play = False
                    break
                if event.key == pygame.K_LEFT:
                    self.character.walkcount += 1
                    if self.character.walkcount == 10:
                        self.character.walkcount = 0
                    if self.character.x > 0:
                        self.character.x -= self.vel
                    else:
                        RELATIVE -= self.vel
                    phase = "walkleft"
                if event.key == pygame.K_RIGHT:
                    self.character.walkcount += 1
                    if self.character.walkcount == 10:
                        self.character.walkcount = 0
                    if self.character.x < 750:
                        self.character.x += self.vel
                    else:
                        RELATIVE += self.vel
                    phase = "walkright"
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    phase = "idleleft"
                if event.key == pygame.K_RIGHT:
                    phase = "idleright"
            pygame.display.update()
        
if __name__ == "__main__":
    g = Graveyard()
    g.game()
