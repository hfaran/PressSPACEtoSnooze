import pygame
from FUGame.utils import utils


class World(object):
    """
    """

    def __init__(self, bg_image, static, NPCs, x, y):
        self.bg_image = bg_image
        self.static = static
        self.NPCs = NPCs
        self._x = x
        self._y = y

    def get_pos(self):
        """Get position of World"""
        return self._x, self._y

    def set_pos(self, x, y):
        """Set position of World"""
        self._x = x
        self._y = y
