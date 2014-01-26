import pygame
from pygame.locals import *

from FUGame.character import Character, Sprite
from FUGame.world import World
from FUGame.constants import *
from FUGame.utils import utils


class EventHandlerMixin:

    def _move_character(self, direction):
        self.world.NPCs["guy"].is_moving = True
        self.world.NPCs["guy"].direction = direction

    @property
    def event_map(self):
        _event_map = {
            K_LEFT: [self._move_character, ("L",)],
            K_RIGHT: [self._move_character, ("R",)],
            K_UP: [self._move_character, ("B",)],
            K_DOWN: [self._move_character, ("F",)]
        }
        return _event_map


class Office(object, EventHandlerMixin):

    def __init__(self):
        self.world = self.create_world

    @property
    def create_world(self):
        # Create objects
        chars = {
            "guy": Character(
                filename="main",
                x=560,
                y=190,
                z=0,
                col_pts=[],
                col_x_offset=50,
                col_y_offset=117,
                fps=10,
                speed=7
            ),
        }

        statics = {
            "officeChairRival": Sprite(
                filename="officeChairRival",
                x=989,
                y=228,
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            )
        }

        world = World(
            level_id="office",
            bg_filename="office_bg_placement_reference",
            static=statics,
            NPCs=chars,
            col_pts=[(57, 504), (76, 504), (110, 504), (137, 502), (164, 502), (172, 478), (174, 441), (185, 404),
                     (191, 363), (207, 329), (210, 291), (253, 295), (296, 293), (329, 296), (374, 289), (422, 294),
                     (464, 295), (511, 291), (534, 291), (555, 312), (550, 341), (557, 393), (546, 111), (546, 142),
                     (546, 180), (546, 209), (758, 391), (757, 359), (753, 311), (752, 262), (761, 209), (753, 163),
                     (753, 106), (807, 291), (854, 286), (892, 289), (935, 293), (971, 294), (1000, 291), (1039, 290),
                     (1078, 291), (1114, 290), (1157, 290), (1166, 329), (1177, 356), (1179, 393), (1189, 431),
                     (1193, 462), (1206, 496), (1239, 503), (1277, 506), (1303, 500)],
            x=0,
            y=0
        )

        world.NPCs["guy"].set_anim("F")

        return world

    def handle_events(self, event):
        keys = pygame.key.get_pressed()

        for key, l in self.event_map.iteritems():
            func, args = l
            if keys[key]:
                func(*args)
                return True
        else:
            self.world.NPCs["guy"].is_moving = False
            return False

    def update_loop(self, screen, game_clock):
        # Create character collision box thing
        sprite_rect = self.world.NPCs["guy"].col_image.get_rect()
        sprite_rect.x, sprite_rect.y = self.world.NPCs["guy"].col_pos

        for s in self.world.sprites:
            if s.is_animating is True:
                self._animate(s)

        for s in self.world.NPCs.values():
            # Movement
            if s.is_moving:
                if not self.world.check_colliding(s):
                    s.move(game_clock.get_fps())
                else:
                    s.set_pos(*s.old_pos)
                self._animate(s)

        #Blitting
        screen.blit(self.world.bg, self.world.pos)

        for s in self.world.sprites:
            screen.blit(s.current_frame, s.pos)


    def _animate(self, s):
        # Animation
        s.update_dt()
        if s.dt.microseconds > 1.0 / s.fps * 1000000:
            s.next_frame()
