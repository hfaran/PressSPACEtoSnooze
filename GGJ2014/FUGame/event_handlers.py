from pygame.locals import *


def key_handle(event):
    _event_map = {
        K_ESCAPE: [exit, (0,)],
    }
    if event.key in _event_map:
        func, args = _event_map[event.key]
        return func(*args)

EVENT_MAP = {
    KEYDOWN: key_handle
}
