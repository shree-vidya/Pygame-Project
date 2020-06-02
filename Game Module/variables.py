# import os
# from PIL import Image, ImageOps

# directory = "C:/Users/ajayv/Desktop/New folder (2)"
# directoryn = "C:/Users/ajayv/Desktop/New folder (2)/Edited"

# # for filename in os.listdir(directory):
# #     if filename.endswith(".png") and filename != "Kunai.png": 
# #          # print(os.path.join(directory, filename))
# #         imag = Image.open(os.path.join(directory, filename))
# #         imag = ImageOps.mirror(image=imag)
# #         imag.save(os.path.join(directoryn, filename))

# l = [(x+1)*5 for x in range(36*2)]
# imag = Image.open(os.path.join(directory, "Kunai.png"))
# for i in l:
#     im = imag.rotate(i, expand=True)
#     im.save(f"Weapon/Kunai_{i}.png")

import pygame
import os
from pygame import mixer

DIRECTORY = "C:/Users/ajayv/Desktop/New folder (2)"

class Assets():
    def __init__(self, levelname, background_image_path):
        # Clock
        self.clock = pygame.time.Clock()
        # Fonts
        self.fonts = {"default" : pygame.font.Font('freesansbold.ttf', 32)}
        # Music
        self.music = {"default": mixer.Sound()}
        

    def setfont(self, font_size, fontname, directory = "freesansbold.ttf"):
        font = pygame.font.Font(directory, font_size)
        self.fonts[fontname] = font

    def setmusic(self, soundname, directory):
        sound = mixer.Sound(directory)
        self.music[soundname] = sound

    def setbackgroundmusic(self, directory):
        mixer.music.load(directory)
        mixer.music.play(-1)


class Character:
    def __init__(self):
        self.characterleft = {}
        self.characterright = {}

        for filename in os.listdir(DIRECTORY + "/Main_character/Left_facing"):
            if filename.endswith(".png"):
                self.characterleft[filename.split(".")[0]] = pygame.image.load(filename)
        
        for filename in os.listdir(DIRECTORY + "/Main_character/Right_facing"):
            if filename.endswith(".png"):
                self.characterright[filename.split(".")[0]] = pygame.image.load(filename)

class Enemy:
    pass

class Layout:
    pass

