from pygame.locals import *


class BaseEventHandlerMixin:
    """Base class with character movement event handling"""
    def _move_character(self, direction):
        if self.allow_move:
            self.world.NPCs["guy"].is_moving = True
            self.world.NPCs["guy"].direction = direction
            return True

    @property
    def _move_event_map(self):
        __move_event_map = {
            K_LEFT: [self._move_character, ("L",)],
            K_RIGHT: [self._move_character, ("R",)],
            K_UP: [self._move_character, ("B",)],
            K_DOWN: [self._move_character, ("F",)],
        }
        return __move_event_map


class Level(object):
    """Base class for Levels"""
    def _animate(self, s):
        # Animation
        s.update_dt()
        if s.dt.microseconds > 1.0 / s.fps * 1000000:
            s.next_frame()
