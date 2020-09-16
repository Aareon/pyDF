from configparser import ConfigParser
import sys

try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    try: import pygame as pygame_sdl2
    except ImportError:
        raise

from loader import load_png


class Item(pygame_sdl2.sprite.Sprite):
    """ Item class, generic class for a sprite """
    def __init__(self, name, tw):
        self.tw = tw
        config = ConfigParser()
        with open('item.cfg') as f:
            config.read_file(f)
        sectionname = 'imagename' + str(self.tw)
        self.movable = True # set this to false to make unmovable items.
        self.selected = False
        self.inqueue = False
        
        imagename = config.get(name, sectionname)
        self.image, self.rect = load_png(imagename)
        self.name = name
        self.surface = pygame_sdl2.transform.scale(self.image, (self.tw, self.tw))
    def __repr__(self):
        return self.name
