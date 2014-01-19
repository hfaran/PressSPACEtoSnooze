import pygame
from MyIsometricGame.utils import utils

class Tile(object):

    def __init__(self, filename, x=0, y=0):
        self.image = utils.convert_white_to_transparent(
            pygame.image.load("assets/tiles/{}.png".format(filename)).convert_alpha())
        self.x = x
        self.y = y

    def get_pos(self):
        return self.x, self.y

    def set_pos(self, x, y):
        self.x = x
        self.y = y
