import pygame
import os

from FUGame.utils import utils
from FUGame.constants import *


class World(object):

    """World class"""

    def __init__(self, level_id, bg_filename, col_pts, static, NPCs, x, y):
        self.bg = pygame.image.load(
            os.path.join(FU_APATH, "backgrounds", bg_filename + ".png")
        )
        self.id = level_id
        self.static = static if static else {}
        self.border_rects = self.get_border_rects()
        self.NPCs = NPCs if NPCs else {}
        self._x = x
        self._y = y
        self.col_pts = col_pts

    def get_border_rects(self):
        rects = []
        rects.append(pygame.Rect(0, 0, 1366, 42))
        rects.append(pygame.Rect(0, 0, 48, 768))
        rects.append(pygame.Rect(0, 630, 1366, 768 - 630))
        rects.append(pygame.Rect(1300, 0, 66, 768))
        return rects

    @property
    def sprites(self):
        """Return all sprites sorted by the z-indices of sprites in
        ascending order
        """
        return sorted(
            [v for v in self.static.values() + self.NPCs.values()],
            key=lambda v: v.z_index
        )

    @property
    def unsorted_sprites(self):
        return [v for v in self.static.values() + self.NPCs.values()]

    @property
    def pos(self):
        """Get position of World"""
        return self._x, self._y

    def set_pos(self, x, y):
        """Set position of World"""
        self._x = x
        self._y = y

    def check_colliding(self, sprite):
        # sprite_rect = sprite.col_image.get_rect()
        # sprite_rect.x, sprite_rect.y = sprite.col_pos
        # for s in [
        #         s for s in self.static.values() + self.NPCs.values()
        #         if s.name != sprite.name]:
        #     if hasattr(s, "col_image"):
        #         s_rect = s.col_image.get_rect()
        #         s_rect.x, s_rect.y = s.col_pos
        #         if s_rect.colliderect(sprite_rect):
        #             return True

        col_rect = sprite.col_rect

        for s in [s for s in self.static.values() + self.NPCs.values() if s.name != sprite.name]:
            for pt in s.col_pts:
                abs_pt = (pt[0] + s.pos[0], pt[1] + s.pos[1])
                if col_rect.collidepoint(abs_pt):
                    return True

        for pt in self.col_pts:
                if col_rect.collidepoint(pt):
                    return True

        sprite_rect = sprite.sprite_rect
        for b in self.border_rects:
            if b.colliderect(sprite_rect):
                    return True
        return False
