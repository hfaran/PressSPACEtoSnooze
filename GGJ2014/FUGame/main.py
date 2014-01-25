import pygame
from FUGame.character import Character
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
    char = Character("test", 0, 0, 5)

    screen.blit(char.current_frame, char.get_pos())
    pygame.display.flip()
    # Game loop
    while True:
        char.update_dt()
        for event in pygame.event.get():
            if event.type in EVENT_MAP:
                func = EVENT_MAP[event.type][0]
                args = EVENT_MAP[event.type][1:]
                func(*args)

        if char.dt.microseconds > 1.0 / char.fps * 1000000:
            print "HIIII"
            char.next_frame()
            screen.blit(char.current_frame, char.get_pos())
            pygame.display.flip()


if __name__ == '__main__':
    main()
