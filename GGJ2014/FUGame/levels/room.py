import pygame
from pygame.locals import *

from FUGame.character import Character
from FUGame.world import World


class Room(object):

    def __init__(self):
        self.world = self.create_world()

    def create_world(self):
        # Create objects
        chars = {
            "guy": Character(
                filename="main",
                x=0,
                y=0,
                z=0,
                fps=5,
                speed=1
            ),
        }
        world = World("room", "room_bg", None, chars, 0, 0)
        return world

    def handle_events(self, event):
        handled = False
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                world.NPCs["guy"].move("L")
                handled = True
        return handled
