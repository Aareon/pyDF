import os
import sys
import random

try:
    import pygame_sdl2
    pygame_sdl2.import_as_pygame()
except ImportError:
    try: import pygame as pygame_sdl2
    except ImportError:
        raise


def load_font(name, size):
    """Load up a font file, or try to use the default None(system font)"""
    fullname = os.path.join('data', name)
    try: 
        font = pygame_sdl2.font.Font(fullname, size)
    except pygame_sdl2.error as message:
        print("Cannot load font file: ", fullname)
    else: 
        font = pygame_sdl2.font.SysFont(None, size)
    return font

def load_sound(name):
    """ Load the sound file from the data directory, return sound """
    fullname = os.path.join('data', name)
    try:
        sound = pygame_sdl2.mixer.Sound(fullname)
    except pygame.error as message:
        print("Cannot load sound file: ", fullname)
        raise SystemExit(message)
    return sound

def load_png(name):
    """ Load image and return image object """
    fullname = os.path.join('data', name)
    try:
        image = pygame_sdl2.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame_sdl2.error as message:
        print('Cannot load image: ', fullname)
        raise SystemExit(message)
    return image, image.get_rect()
