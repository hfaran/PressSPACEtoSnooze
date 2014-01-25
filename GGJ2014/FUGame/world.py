import pygame
import os

from FUGame.utils import utils
from FUGame.constants import *


class World(object):

    """World class"""

    def __init__(self, level_id, bg_filename, static, NPCs, x, y):
        self.bg = pygame.image.load(
            os.path.join(FU_APATH, "backgrounds", bg_filename + ".png")
        )
        self.id = level_id
        self.static = static if static else {}
        self.NPCs = NPCs if NPCs else {}
        self._x = x
        self._y = y

    @property
    def sprites(self):
        """Return all sprites sorted by the z-indices of sprites in
        ascending order
        """
        return sorted(
            [v for v in self.static.values() + self.NPCs.values()],
            key=lambda v: v.z
        )

    @property
    def pos(self):
        """Get position of World"""
        return self._x, self._y

    def set_pos(self, x, y):
        """Set position of World"""
        self._x = x
        self._y = y

    # def handle_input(self, event_type):
    #     d =
