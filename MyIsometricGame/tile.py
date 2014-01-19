import pygame
from MyIsometricGame.utils import utils

class Tile(object):

    def __init__(self, filename, x=0, y=0):
        self.image = utils.convert_white_to_transparent(
            pygame.image.load("assets/tiles/{}.png".format(filename)).convert_alpha())
        self.mask = pygame.mask.from_surface(self.image)
        self._x = x
        self._y = y

    def get_pos(self):
        return self._x, self._y

    def set_pos(self, x, y):
        self._x = x
        self._y = y

    def point_collision(self, pos):
        try:
            return self.mask.get_at(pos)
        except IndexError:
            return False
