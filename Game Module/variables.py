import os
from PIL import Image, ImageOps

directory = "C:/Users/ajayv/Desktop/New folder (2)"
directoryn = "C:/Users/ajayv/Desktop/New folder (2)/Edited"

# for filename in os.listdir(directory):
#     if filename.endswith(".png") and filename != "Kunai.png": 
#          # print(os.path.join(directory, filename))
#         imag = Image.open(os.path.join(directory, filename))
#         imag = ImageOps.mirror(image=imag)
#         imag.save(os.path.join(directoryn, filename))

l = [(x+1)*5 for x in range(36*2)]
imag = Image.open(os.path.join(directory, "Kunai.png"))
for i in l:
    im = imag.rotate(i, expand=True)
    im.save(f"Weapon/Kunai_{i}.png")

        