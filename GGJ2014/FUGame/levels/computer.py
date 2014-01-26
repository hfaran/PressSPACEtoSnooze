import pygame
from pygame.locals import *

import os
from random import choice

from FUGame.character import Character, Sprite
from FUGame.world import World
from FUGame.constants import *
from FUGame.utils import utils
from FUGame.levels.level import Level, BaseEventHandlerMixin


class EventHandlerMixin(BaseEventHandlerMixin):

    def _use(self):
        pass

    @property
    def event_map(self):
        _event_map = dict(self._move_event_map)
        _event_map[K_SPACE] = [self._use, ()]
        return _event_map


class Computer(Level, EventHandlerMixin):
    def __init__(self):
        self.world = self.create_world()
        # Code to display
        self._code = filter(
            lambda x: x,
            open(os.path.join("FUGame", "levels", "computer.py"), "r").read().split()
        )
        self._code_rect = pygame.Rect(500,300,300,300)
        self._code_font = pygame.font.SysFont("courier_new", 20)


    def create_world(self):
        world = World(
            level_id="computerScreen",
            bg_filename="computerScreen_bg",
            static=None,
            NPCs=None,
            col_pts=[],
            x=0,
            y=0
        )
        return world

    def handle_events(self, event):
        pass

    def update_loop(self, screen, game_clock):
        self._draw_code(screen)
        # Blitting
        self._blit(screen)

    def _blit(self, screen):
        screen.blit(self.world.bg, self.world.pos)

    def _draw_code(self, screen):
        utils.drawText(
            screen,
            "\n".join([choice(self._code) for i in xrange(5)]),
            (0,255,0),
            self._code_rect,
            self._code_font,
            aa=True
            )

