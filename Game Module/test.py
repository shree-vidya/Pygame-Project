import os
from PIL import Image

Filepath = os.getcwd()
Charpath = os.path.join(Filepath, "Main_character", "Left_facing")

for filename in os.listdir(Charpath):
    if filename.endswith(".png"):
        imag = Image.open(os.path.join(Charpath, filename))
        x, y = imag.size
        imag = imag.resize((x//4,y//4))
        imag.save(os.path.join(Filepath, "Main_character", "Edited", filename))

Charpath = os.path.join(Filepath, "Main_character", "Right_facing")

for filename in os.listdir(Charpath):
    if filename.endswith(".png"):
        imag = Image.open(os.path.join(Charpath, filename))
        x, y = imag.size
        imag = imag.resize((x//4,y//4))
        imag.save(os.path.join(Filepath, "Main_character", "Edited_Right", filename))