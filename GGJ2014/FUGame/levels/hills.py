import pygame
import os
from pygame.locals import *

from FUGame.character import Character, Sprite
from FUGame.world import World
from FUGame.constants import *
from FUGame.utils import utils

from random import randint


class EventHandlerMixin:

    @property
    def event_map(self):
        _event_map = {
            K_LEFT: [self._move_character, ("L",)],
            K_RIGHT: [self._move_character, ("R",)],
            K_UP: [self._move_character, ("B",)],
            K_DOWN: [self._move_character, ("F",)],
        }
        return _event_map


class Hills(object, EventHandlerMixin):

    def __init__(self):
        self.world = self.create_world()

    def create_world(self):
        chars = {
            "guy": Character(
                filename="main",
                x=525,
                y=190,
                z=0,
                col_pts=[],
                col_x_offset=50,
                col_y_offset=117,
                fps=10,
                speed=0.2
            ),
        }
        statics = {

        }
        world = World(
            level_id="hills",
            bg_filename="hills_bg",
            static=statics,
            NPCs=chars,
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
        else:
            self.world.NPCs["guy"].is_moving = False
            return False

    def update_loop(self, screen, game_clock):
        raise NotImplementedError
