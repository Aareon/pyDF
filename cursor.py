import configparser
import os

from loader import load_png


class Cursor():
    """ Cursor class, generic class for a Cursor """
    def __init__(self, tw, x, y):
        self.tw = tw
        self.position = [x, y]
        self.mapx = 0
        self.mapy = 0
        config = configparser.ConfigParser()
        with open('cursor.cfg') as f:
            config.read_file(f)
        
        imagename = config.get('cursor', "imagename" + str(tw))
        self.image, self.rect = load_png(imagename)
    
