from pygame.locals import *
from FUGame.constants import *
import pygame
from datetime import datetime


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

    def _animate(self, s, anim_once=False):
        # Animation
        s.update_dt()
        if s.dt.microseconds > 1.0 / s.fps * 1000000:
            if not anim_once:
                s.next_frame()
            elif anim_once and s.current_frame_num + 1 < len(s.anims[s.current_anim]):
                s.is_animating = s.next_frame()

    def _animate_sprites(self):
        for s in self.world.unsorted_sprites:
            if s.is_animating is True:
                self._animate(s)

    def _move_npcs(self, game_clock):
        for s in self.world.NPCs.values():
            # Movement
            if s.is_moving:
                if not self.world.check_colliding(s):
                    s.move(game_clock.get_fps())
                else:
                    s.set_pos(*s.old_pos)
                self._animate(s)

    class Credits:
        def __init__(self):
            self.credit_font = pygame.font.SysFont("verdana", 24)
            self.alpha = 0
            self.texts = list(reversed([self.credit_font.render(FU_CREDITS[i], True, (255, 255, 255)) for i in xrange(len(FU_CREDITS))]))
            self.rect = pygame.Surface((FU_WIDTH, FU_HEIGHT))
            self.rect.fill((0, 0, 0))
            self.rect.set_alpha(self.alpha)
            self.credits_pos = ((FU_WIDTH/2, FU_HEIGHT * 1.75))
            self.texts_pos = self._texts_positions()
            self.speed = 3
            self.fps = 30
            self.spacing = 40
            self.lastdt = datetime.now()
            self.update_dt()
            self.end = False

        def update_dt(self):
            self.dt = datetime.now() - self.lastdt

        def darken(self):
            if self.alpha <= 250:
                self.alpha += self.speed
                self.rect.set_alpha(self.alpha)

        def scroll_credits(self):
            self.credits_pos = self.credits_pos[0], self.credits_pos[1] - self.speed
            self.texts_pos = self._texts_positions()
            if self.credits_pos[1] + 40*len(FU_CREDITS) < 550:
                self.end = True

        def update_credits(self):
            self.scroll_credits()
            self.darken()
            self.lastdt = datetime.now()

        def _texts_positions(self):
            return [
                (self.credits_pos[0] - self.texts[i].get_width()/2, self.credits_pos[1] - 40*i)
                for i in xrange(len(FU_CREDITS))]
