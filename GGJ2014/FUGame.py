#!/usr/bin/env python2.7

import pygame
from pygame.locals import *

from importlib import import_module
from itertools import chain

from FUGame.constants import *
from FUGame.event_handlers import EVENT_MAP
from FUGame.character import Character
from FUGame.world import World
from FUGame import levels


class Game(object):

    def __init__(self):
        pygame.init()
        # screenInfo = pygame.display.Info()
        # screen = pygame.display.set_mode(
        #     (screenInfo.current_w, screenInfo.current_h),
        #     pygame.FULLSCREEN
        # )
        self.screen = pygame.display.set_mode(
            (FU_WIDTH, FU_HEIGHT),
        )
        pygame.display.set_caption('FUGame')

        # Levels
        self.levels = FU_LEVELS

    def loop(self):
        self.level.update_loop(self.screen)

        # self.screen.blit(self.level.world.bg, self.level.world.pos)
        # for s in self.level.world.sprites:
        #     self.screen.blit(s.current_frame, s.pos)

        self.handle_events()

    def handle_events(self):
        for event in pygame.event.get():
            if self.level.handle_events(event):
                return True
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                exit(0)
            elif event.type in EVENT_MAP:
                func = EVENT_MAP[event.type][0]
                args = EVENT_MAP[event.type][1:]
                func(*args)
                return True
        else:
            return False

    def create_level(self, level_name):
        level_mod = import_module("FUGame.levels." + level_name)
        level_class = getattr(
            level_mod, level_name[0].upper() + level_name[1:])
        level = level_class()
        return level

    def main(self):
        self.current_level = self.levels[0]
        self.level = self.create_level(self.current_level)

        # Game loop
        while True:
            self.loop()
            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.main()
