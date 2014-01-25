import pygame
from FUGame.character import Character
from FUGame.world import World
from pygame.locals import *

from itertools import chain

from FUGame.constants import *
from FUGame.event_handlers import EVENT_MAP


def initialize():
    """Initialize game etc."""
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
    return screen


def create_world():
    # Create objects
    chars = {
        "guy": Character("main", 0, 0, 5, speed=1),
    }
    world = World("room", "room_bg", None, chars, 0, 0)
    return world


def loop(screen, world):
    screen.blit(world.bg, world.pos)
    for s in world.sprites:
        screen.blit(s.current_frame, s.pos)

    handle_events()


def handle_events():
    for event in pygame.event.get():
        if event.type in EVENT_MAP:
            func = EVENT_MAP[event.type][0]
            args = EVENT_MAP[event.type][1:]
            func(*args)


def main():
    screen = initialize()
    world = create_world()

    # Game loop
    while True:
        loop(screen, world)
        # char.update_dt()
        # if char.dt.microseconds > 1.0 / char.fps * 1000000:
        #     print "HIIII"
        #     char.next_frame()
        #     screen.blit(char.current_frame, char.get_pos())
        #     pygame.display.flip()
        pygame.display.flip()

if __name__ == '__main__':
    main()
