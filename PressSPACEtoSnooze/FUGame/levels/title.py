import pygame
from pygame.locals import *

from FUGame.world import World
from FUGame.constants import *
from FUGame.utils import utils
from FUGame.levels.level import Level, BaseEventHandlerMixin


class EventHandlerMixin(BaseEventHandlerMixin):

    def _use(self):
        raise utils.NextLevelException("instructions", 0)

    @property
    def event_map(self):
        _event_map = dict(self._move_event_map)
        _event_map[K_RETURN] = [self._use, ()]
        return _event_map


class Title(Level, EventHandlerMixin):

    def __init__(self, state=0):
        self.world = self.create_world()

    def create_world(self):
        world = World(
            level_id="title",
            bg_filename="title_bg",
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
        screen.fill((0, 0, 0))
        screen.blit(self.world.bg, self.world.pos)
