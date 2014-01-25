import pygame
from pygame.locals import *

from FUGame.character import Character, Sprite
from FUGame.world import World


class Room(object):

    def __init__(self):
        self.world = self.create_world()

    def create_world(self):
        # Create objects
        chars = {
            "guy": Character(
                filename="main",
                x=210,
                y=210,
                z=0,
                col_pts=[],
                col_x_offset=7,
                col_y_offset=92,
                fps=10,
                speed=5
            ),
        }
        statics = {
            "desk": Sprite(
                filename="desk",
                x=1075,
                y=210,
                z=0,
                col_pts=[(4, 61), (17, 120), (27, 171), (40, 221), (56, 294), (69, 56), (120, 293), (182, 293), (131, 56)],
                col_x_offset=None,
                col_y_offset=None
            )
        }
        world = World(
            level_id="room",
            bg_filename="room_bg",
            static=statics,
            NPCs=chars,
            col_pts=[(49, 630), (63, 555), (75, 500), (48, 464), (95, 370), (65, 305), (49, 267), (115, 280),
                     (130, 210), (195, 210), (260, 210), (325, 210), (390, 210), (455, 210), (520, 210), (585, 210),
                     (650, 210), (715, 210), (780, 210), (845, 210), (910, 210), (975, 210), (1040, 210), (1105, 210),
                     (1170, 210), (1200, 210), (1210, 265), (1220, 305), (1255, 500), (1270, 560), (1280, 630)],
            x=0,
            y=0
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
                if not self.world.check_colliding(s):
                    s.move()
                else:
                    s.set_pos(*s.old_pos)
                self._animate(s)

    def _animate(self, s):
        # Animation
        s.update_dt()
        if s.dt.microseconds > 1.0 / s.fps * 1000000:
            s.next_frame()
