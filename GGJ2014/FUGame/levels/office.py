import pygame
from pygame.locals import *

from FUGame.character import Character, Sprite
from FUGame.world import World
from random import randint


class EventHandlerMixin:

    def _move_character(self, direction):
        self.world.NPCs["guy"].is_moving = True
        self.world.NPCs["guy"].direction = direction

    @property
    def event_map(self):
        _event_map = {
            K_LEFT: [self._move_character, ("L",)],
            K_RIGHT: [self._move_character, ("R",)],
            K_UP: [self._move_character, ("B",)],
            K_DOWN: [self._move_character, ("F",)]
        }
        return _event_map


class Office(object, EventHandlerMixin):

    def _init_(self):
        self.world = self.create_world()

    def create_world(self):
        # Create objects
        chars = {
            "guy": Character(
                filename="main",
                x=560,
                y=190,
                z=0,
                col_pts=[],
                col_x_offset=7,
                col_y_offset=92,
                fps=4,
                speed=5
            ),
        }

        statics = {

        }

        world = World(
            level_id="office",
            bg_filename="office_bg",
            static=statics,
            NPCs=chars,
            col_pts=[(60, 500), (100, 500), (160, 500), (172, 446), (200, 366), (211, 291), (275, 293), (540, 293),
                     (0, 0)],
            x=0,
            y=0
        )

        world.NPCs["guy"].set_anim("F")

        return world

    def handle_events(self, event):
        keys = pygame.key.get_pressed()
        for key, l in self.event_map.iteritems():
            func, args = l
            if keys[key]:
                func(*args)
                return True
        else:
            self.world.NPCs["guy"].is_moving = False
            return False


