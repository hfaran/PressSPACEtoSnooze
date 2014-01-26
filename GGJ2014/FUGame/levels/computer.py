import pygame
from pygame.locals import *

import os
from random import choice
from datetime import datetime

from FUGame.character import Character, Sprite
from FUGame.world import World
from FUGame.constants import *
from FUGame.utils import utils
from FUGame.levels.level import Level, BaseEventHandlerMixin


class EventHandlerMixin(BaseEventHandlerMixin):

    def _use(self):
        if self.display_cmd:
            self.disp_time = datetime.now()
            self.display_cmd = False
            self._space_count += 1
            self._code_text = self.get_code_text()

    @property
    def event_map(self):
        _event_map = dict(self._move_event_map)
        _event_map[K_SPACE] = [self._use, ()]
        return _event_map


class Computer(Level, EventHandlerMixin):

    def __init__(self):
        self.world = self.create_world()
        # Clock stuff
        self._scroll_delay = 2.0
        self._wait_to_win_delay = 8.0
        self.disp_time = datetime.now()
        # Press Space to do stuff bar
        self.display_cmd = True
        self._space_message = 'Press SPACE to Work'
        self._space_rect = pygame.Rect(FU_CMD_POS[0], FU_CMD_POS[1], 1280, 300)
        self._space_font = pygame.font.SysFont("verdana", 48)
        self._space_count = 1
        # Code to display
        self._code = filter(
            lambda x: x,
            open(os.path.join("FUGame", "levels", "computer.py"),
                 "r").read().split("\n")
        )
        self._code_text = self.get_code_text()
        self._code_rect = pygame.Rect(250, 100, 750, 500)
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
        keys = pygame.key.get_pressed()
        for key, l in self.event_map.iteritems():
            func, args = l
            if keys[key]:
                return bool(func(*args))

    def update_loop(self, screen, game_clock):
        # Blitting
        self._blit(screen)

    def _blit(self, screen):
        screen.blit(self.world.bg, self.world.pos)
        self._draw_code(screen)
        if self.display_cmd:
            self._draw_space(screen)

        if (datetime.now() - self.disp_time).total_seconds() > self._wait_to_win_delay:
            raise utils.NextLevelException("office", 0)
        elif (datetime.now() - self.disp_time).total_seconds() > self._scroll_delay:
            if not self.display_cmd:
                self.display_cmd = True

    def get_code_text(self):
        # return (" " * 10).join([choice(self._code) for i in
        # xrange(len(self._code))])
        return ("; ").join(self._code[26:self._space_count + 26])

    def _draw_space(self, screen):
        utils.drawText(
            screen,
            self._space_message,
            FU_CMD_COLOR,
            self._space_rect,
            self._space_font,
            aa=True
        )

    def _draw_code(self, screen):
        utils.drawText(
            screen,
            self._code_text,
            (0, 255, 0),
            self._code_rect,
            self._code_font,
            aa=True
        )
