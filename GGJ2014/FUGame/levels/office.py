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
            "officeChairMain": Sprite(
                filename="officeChairMain",
                x=288,
                y=278,
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),

            "officeChairRival": Sprite(
                filename="officeChairRival",
                x=989,
                y=228,
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),

            "garbageCan": Sprite(
                filename="garbageCan",
                x=1108,
                y=450,
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),

            "sparks": Sprite(
                filename="sparks",
                x=665,
                y=535,
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),

            "computerBlink": Sprite(
                filename="computerBlink",
                x=450,
                y=285,
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),

            "officeWalls": Sprite(
                filename="officeWalls",
                x=0,
                y=0,
                z=1,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            )
        }

        world = World(
            level_id="office",
            #bg_filename="office_bg_placement_reference",
            bg_filename="office_bg",
            static=statics,
            NPCs=chars,
            col_pts=[
            (67, 497), (107, 497), (124, 493), (155, 493), (171, 481), (181, 439), (190, 382), (207, 334), (207, 304),
            (220, 285), (257, 275), (298, 275), (347, 275), (395, 275), (450, 285), (459, 330), (508, 331), (538, 351),
            (548, 272), (565, 251), (566, 179), (725, 214), (744, 277), (744, 348), (770, 305), (819, 309), (858, 305),
            (923, 305), (990, 302), (1057, 299), (1116, 303), (1137, 326), (1153, 393), (1169, 452), (1178, 521),
            (1225, 517), (1299, 516)],
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
