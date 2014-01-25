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
        world = World(
            "room",
            "room_bg",
            None,
            chars,
            0,
            0
        )
        return world

    def handle_events(self, event):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.world.NPCs["guy"].is_moving = True
            self.world.NPCs["guy"].direction = "L"
            return True
        if keys[K_RIGHT]:
            self.world.NPCs["guy"].is_moving = True
            self.world.NPCs["guy"].direction = "R"
            return True
        if keys[K_DOWN]:
            self.world.NPCs["guy"].is_moving = True
            self.world.NPCs["guy"].direction = "F"
            return True
        if keys[K_UP]:
            self.world.NPCs["guy"].is_moving = True
            self.world.NPCs["guy"].direction = "B"
            return True
        else:
            self.world.NPCs["guy"].is_moving = False
        return False

    def update_loop(self):
        for s in self.world.NPCs.values():
            # Movement
            if s.is_moving:
                s.move()
                self._animate(s)

    def _animate(self, s):
        # Animation
        s.update_dt()
        if s.dt.microseconds > 1.0 / s.fps * 1000000:
            s.next_frame()
