import os
import pygame

GAMEPATH = os.getcwd()
PATH = os.path.join(GAMEPATH, "Theme", "Graveyard", "tiles")

TILES = {
            "1":{
                "1":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (11).png")),
                    "hitbox" : (0,750 - 128), #x1, y1 
                    "x" : 0
                },
                "2":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (2).png")),
                    "hitbox" : (128,750 - 128), #x, y
                    "x" : 128
                },
                "3":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (2).png")),
                    "hitbox" : (128*2,750 - 128), #x, y
                    "x" : 128*2
                },
                "4":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (2).png")),
                    "hitbox" : (128*3,750 - 128), #x, y
                    "x" : 128*3
                },
                "5":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (2).png")),
                    "hitbox" : (128*4,750 - 128), #x, y
                    "x" : 128*4
                },
                "6":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (3).png")),
                    "hitbox" : (128*5,750 - 128), #x, y
                    "x" : 128*5
                }
            },
            "2":{
                "1":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (11).png")),
                    "hitbox" : (0,200), #x, y
                    "x" : 0
                },
                "2":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (3).png")),
                    "hitbox" : (128,200), #x, y
                    "x" : 128
                },
                "3":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (5).png")),
                    "hitbox" : (0,200 + 128), #x, y
                    "x" : 0
                },
                "4":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (10).png")),
                    "hitbox" : (128,200 + 128), #x, y
                    "x" : 128
                },
                "5":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (11).png")),
                    "hitbox" : (128*2,200 + 128), #x, y
                    "x" : 128*2
                },
                "6":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (3).png")),
                    "hitbox" : (128*3,200 + 128), #x, y
                    "x" : 128*3
                },
                "7":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Bone (1).png")),
                    "hitbox" : (0,200 + 128), #x, y
                    "x" : 0
                }
            },
            "3":{
                "1":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (14).png")),
                    "hitbox" : (128*5,175), #x, y
                    "x" : 128*5
                },
                "2":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (15).png")),
                    "hitbox" : (128*6,175), #x, y
                    "x" : 128*6
                },
                "3":{ 
                    "Resource": pygame.image.load(os.path.join(PATH, "Tile (16).png")),
                    "hitbox" : (128*7,175), #x, y
                    "x" : 128*7
                }
            }
        }

DECORATIONS = {}


CROSSHAIR = (
  "           X            ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           ..           ",
  "                        ",
  "           ..           ",
  " XXXXXXX. .XX. .XXXXXXXX",
  "XXXXXXXX. .XX. .XXXXXXX ",
  "           ..           ",
  "                        ",
  "           ..           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "           XX           ",
  "            X           "
)