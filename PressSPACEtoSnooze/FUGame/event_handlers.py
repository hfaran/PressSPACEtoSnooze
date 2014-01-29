import pygame
import sys
from pygame.locals import *

from FUGame.constants import *


def noop(*args, **kwargs):
    pass


def quit(event):
    exit(0)


def key_handle(event):
    _event_map = {
        K_ESCAPE: [exit if FU_FULLSCREEN else noop, (0,)],
    }
    if event.key in _event_map:
        func, args = _event_map[event.key]
        return func(*args)


def click_handle(event):
    if all([pygame.mouse.get_pressed()[0], FU_DEBUG]):
        s = '(%d, %d), ' % (event.pos[0], event.pos[1])
        sys.stdout.write(s)

EVENT_MAP = {
    QUIT: quit
    KEYDOWN: key_handle,
    MOUSEBUTTONDOWN: click_handle
}
