import configparser
import os
import pprint
import sys
from time import time

try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    try: import pygame as pygame_sdl2
    except ImportError:
        raise

from loader import load_png


class Mob(pygame_sdl2.sprite.Sprite):
    """ Mob class, generic class for a sprite """
    def __init__(self, position, tw, name=None):
        self.tw = tw
        config = configparser.ConfigParser()
        with open('mob.cfg') as f:
            config.read_file(f)

        imageset = 'imagename' + str(self.tw)
        imagename = config.get('mob', imageset)
        self.image, self.rect = load_png(imagename)
        self.position = position
        self.miningskill = 5
        self.name = name or "Jimmy"
        self.surface = pygame_sdl2.transform.scale(self.image, (self.tw, self.tw))
        self.pathlines = []
        self.job = None
        self.skillcounter = 0
        self.carrying = None

    def pickupitem(self, item):
        self.carrying = item

    def __repr__(self):
        return self.name
