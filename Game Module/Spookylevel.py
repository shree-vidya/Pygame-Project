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
        self.background = pygame.image.load(GAMEPATH + "/Theme/Graveyard/BG.png")

    def getscreen(self):
        return self.screen


class Character:
    def __init__(self):
        self.characterleft = {}
        self.characterright = {}

        for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Left_facing")):
            if filename.endswith(".png"):
                self.characterleft[filename.split(".")[0]] = pygame.image.load(filename)
        
        for filename in os.listdir(os.path.join(GAMEPATH, "Main_character", "Right_facing")):
            if filename.endswith(".png"):
                self.characterright[filename.split(".")[0]] = pygame.image.load(filename)

class Enemy:
    pass

class Layout(Assets):
    def __init__(self, screen):
        self.screen = screen
        self.decorations = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Objects", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Objects"))
        }
        self.tiles = {
            filename.split(".")[0] : pygame.image.load(os.path.join(THEMEPATH, "Tiles", filename)) for filename in os.listdir(os.path.join(THEMEPATH, "Tiles"))
        }

    def loadfloors(self):
        self.screen.blit(self.tiles['Tile (14)'], (300,300))
        self.screen.blit(self.tiles['Tile (15)'], (300+128,300))
        self.screen.blit(self.tiles['Tile (16)'], (300+128*2,300))
        self.screen.blit(self.tiles['Tile (14)'], (1000,300))
        self.screen.blit(self.tiles['Tile (15)'], (1000+128,300))
        self.screen.blit(self.tiles['Tile (16)'], (1000+128*2,300))
        self.screen.blit(self.decorations['Tree'], (10,750-128-239))
        self.screen.blit(self.decorations['TombStone1'], (400,300-55))
        self.screen.blit(self.decorations['TombStone2'], (1100,300-76))
        for i in range(1500//128 + 1):
            self.screen.blit(self.tiles['Tile (2)'], (128*i,750-128))

class Graveyard:
    def __init__(self):
        pygame.init()
        self.asset = Assets()
        param = self.asset.getscreen()
        self.layout = Layout(param)

    def setup(self):
        self.screen = pygame.display.set_mode((1500, 750))
        pygame.display.set_caption("Level 3: Graveyard") 
        self.background = self.asset.background
    
    def game(self):
        self.setup()
        self.play = True

        while self.play:
            self.screen.fill((0,0,0))
            self.screen.blit(self.background, (0,0))
            self.layout.loadfloors()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play = False
            pygame.display.update()
        
if __name__ == "__main__":
    g = Graveyard()
    g.game()
