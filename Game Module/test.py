import os
from PIL import Image, ImageOps

directory = "C:/Users/ajayv/Desktop/New folder (2)/Main_character/Left_facing"
for filename in os.listdir(directory):
    if filename.endswith(".png"): 
        print(filename)