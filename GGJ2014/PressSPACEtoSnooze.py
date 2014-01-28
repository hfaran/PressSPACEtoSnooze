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
from FUGame.utils import utils


class Game(object):

    def __init__(self):
        #pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        # screenInfo = pygame.display.Info()
        # screen = pygame.display.set_mode(
        #     (screenInfo.current_w, screenInfo.current_h),
        #     pygame.FULLSCREEN
        # )
        self.screen = pygame.display.set_mode(
            (FU_WIDTH, FU_HEIGHT),
        )
        pygame.display.set_caption('Press \'SPACE\' to Snooze')
        self.clock = pygame.time.Clock()

        # Levels
        self.levels = FU_LEVELS

    def loop(self):
        self.screen.fill((0, 0, 0))
        self.clock.tick(FU_FRAME_RATE)
        self.level.update_loop(self.screen, self.clock)
        # self.screen.blit(self.level.world.bg, self.level.world.pos)
        # for s in self.level.world.sprites:
        #     self.screen.blit(s.current_frame, s.pos)
        self.handle_events()

    def handle_events(self):
        for event in pygame.event.get():
            if self.level.handle_events(event):
                return True
            elif event.type in EVENT_MAP:
                func = EVENT_MAP[event.type]
                func(event)
                return True
        else:
            return False

    def create_level(self, level_name, state=0):
        level_mod = import_module("FUGame.levels." + level_name)
        level_class = getattr(
            level_mod, level_name[0].upper() + level_name[1:])
        level = level_class(state)
        return level

    def main(self):
        # Create initial level
        self.current_level = self.levels[0]
        self.level = self.create_level(self.current_level)
        # Game loop
        while True:
            # Call self.loop() continuously, until it raises
            # a NextLevelException with info on what level to load next
            try:
                self.loop()
                pygame.display.flip()
            except utils.NextLevelException as e:
                self.current_level = e.next_level
                self.level = self.create_level(self.current_level, e.state)


if __name__ == '__main__':
    game = Game()
    game.main()
