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

        self.old_x = self._x
        self.old_y = self._y

    @property
    def old_pos(self):
        return self.old_x, self.old_y

    def move(self, fps):
        """Moves Character at a speed normalized by `fps` for a consistent
        experience
        """
        self.current_anim = self.direction
        self.old_x, self.old_y = self.pos
        self.set_pos(
            self.pos[0] + FU_DIRECTS[self.direction][0] * self.speed * (2 - fps / (FU_FRAME_RATE * 1.5)),
            self.pos[1] + FU_DIRECTS[self.direction][1] * self.speed * (2 - fps / (FU_FRAME_RATE * 1.5))
        )
