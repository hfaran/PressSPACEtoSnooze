import pygame
from FUGame.sprite import Sprite
from FUGame.utils import utils
from FUGame.constants import *


class Character(Sprite):

    """
    """

    def __init__(self, *args, **kwargs):
        speed = kwargs.pop('speed', None)
        if not speed:
            raise KeyError("Missing required parameter `speed`")
        super(Character, self).__init__(*args, **kwargs)
        self.speed = speed

    def move(self, direction):
        self.set_pos(self.pos + FU_DIRECTS[direction] * self.speed)
