import pygame
from FUGame.sprite import Sprite
from FUGame.utils import utils
from FUGame.constants import *


class Character(Sprite):

    """Character class"""

    def __init__(self, *args, **kwargs):
        speed = kwargs.pop('speed', None)
        if not speed:
            raise KeyError("Missing required parameter `speed`")
        super(Character, self).__init__(*args, **kwargs)

        self.speed = speed
        self.direction = "L"

    def move(self):
        self.current_anim = self.direction
        self.set_pos(self.pos[0] + FU_DIRECTS[self.direction][0] * self.speed,
                     self.pos[1] + FU_DIRECTS[self.direction][1] * self.speed)
