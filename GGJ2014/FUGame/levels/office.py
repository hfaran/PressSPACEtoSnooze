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
    pass