import pygame
from pygame.locals import *

from itertools import chain

from FUGame.constants import *
from FUGame.event_handlers import EVENT_MAP

def main():
    # Initialize game etc.
    pygame.init()
    # screenInfo = pygame.display.Info()
    # screen = pygame.display.set_mode(
    #     (screenInfo.current_w, screenInfo.current_h),
    #     pygame.FULLSCREEN
    # )
    screen = pygame.display.set_mode(
        (FU_WIDTH, FU_HEIGHT),
    )
    pygame.display.set_caption('FUGame')

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type in EVENT_MAP:
                func = EVENT_MAP[event.type][0]
                args = EVENT_MAP[event.type][1:]
                func(*args)


if __name__ == '__main__':
    main()
