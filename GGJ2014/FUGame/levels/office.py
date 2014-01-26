import pygame
from pygame.locals import *

from FUGame.character import Character, Sprite
from FUGame.world import World
from FUGame.constants import *
from FUGame.utils import utils
from FUGame.levels.level import Level, BaseEventHandlerMixin


class EventHandlerMixin(BaseEventHandlerMixin):
    # @property
    # def seqd(self):
    #     """Sequence dict"""
    #     return {
    #         "sit_chair":
    #     }

    def _use(self):

        for s in self.world.static.values():
                if s.use_func and s.sprite_rect.colliderect(
                        self.world.NPCs["guy"].sprite_rect):
                    s.use_func()
                elif s.name == "garbageCan" and s.sprite_rect.colliderect(
                        self.world.NPCs["guy"].sprite_rect):
                            s.is_animating = True


    @property
    def event_map(self):
        _event_map = dict(self._move_event_map)
        _event_map[K_SPACE] = [self._use, ()]
        return _event_map


class Office(Level, EventHandlerMixin):
    def __init__(self):
        self.world = self.create_world()

        self.allow_move = True
        self.sparked = False
        self.credits = self.Credits()

    def create_world(self):
        # Create objects
        chars = {
            "guy": Character(
                filename="main",
                x=560,
                y=90,
                z=0,
                col_pts=[],
                col_x_offset=50,
                col_y_offset=117,
                fps=10,
                speed=7
            ),
            "rival": Character(
                filename="rival",
                x=1020,
                y=95,
                z=100,
                col_pts=[],
                col_x_offset=0,
                col_y_offset=0,
                fps=10,
                speed=5
            )
        }

        statics = {
            "officeChairMain": Sprite(
                filename="officeChairMain",
                x=288,
                y=278,
                z=0,
                col_pts=[(60, 0), (80, 0), (100, 0), (120, 0), (132, 0),
                         (0, 80), (0, 100), (0, 109),
                         (20, 109), (40, 109), (60, 109), (80, 109), (100, 109), (120, 109), (132, 109),
                         (132, 80), (132, 100), (132, 109)],
                col_x_offset=None,
                col_y_offset=None
            ),

            "officeChairRival": Sprite(
                filename="officeChairRival",
                x=989,
                y=228,
                z=0,
                col_pts=[(0, 0), (30, 0), (60, 0), (90, 0), (120, 0), (150, 0), (172, 0), (172, 166),
                         (0, 30), (0, 60), (0, 90), (0, 120), (0, 150), (0, 166),
                         (172, 30), (172, 60), (172, 90), (172, 120), (172, 150),
                         (0, 166), (30, 166), (60, 166), (90, 166), (120, 166), (150, 166)
                ],
                col_x_offset=None,
                col_y_offset=None,
            ),

            "garbageCan": Sprite(
                filename="garbageCan",
                x=1108,
                y=460,
                z=0,
                col_pts=[(97, 59), (0, 59), (7, 21), (44, 0), (77, 11), (90, 29)],
                col_x_offset=None,
                col_y_offset=None,
            ),

            "sparks": Sprite(
                filename="sparks",
                x=665,
                y=535,
                z=0,
                col_pts=[(0, 0), (0, 42), (49, 0), (49, 42)],
                col_x_offset=None,
                col_y_offset=None,
                fps=10
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
            col_pts=[(58, 495), (83, 495), (109, 495), (136, 495), (165, 495), (171, 468), (175, 435), (187, 402),
                     (188, 369), (193, 347), (205, 318), (209, 288), (213, 279), (245, 275), (261, 275), (276, 275),
                     (296, 273), (324, 273), (359, 273), (383, 273), (418, 278), (428, 292), (436, 327), (455, 328),
                     (491, 331), (519, 334), (532, 349), (552, 345), (553, 330), (555, 312), (555, 294), (554, 271),
                     (554, 253), (568, 220), (564, 198), (565, 175), (567, 146), (567, 120), (567, 90), (567, 56),
                     (567, 50), (718, 53), (719, 70), (719, 101), (717, 133), (714, 175), (720, 219), (722, 251),
                     (726, 264), (738, 294), (737, 334), (745, 350), (761, 339), (769, 319), (793, 311), (814, 311),
                     (835, 306), (856, 306), (870, 305), (901, 300), (928, 293), (944, 295), (982, 299), (994, 301),
                     (1045, 296), (1067, 293), (1110, 289), (1140, 316), (1124, 358), (1152, 380), (1166, 410),
                     (1166, 437), (1174, 446), (1187, 466), (1188, 482), (1211, 499), (1239, 491), (1261, 490),
                     (1285, 490), (1298, 488)],
            x=0,
            y=0
        )

        world.NPCs["guy"].set_anim("F")
        world.static["sparks"].is_animating = True

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
        self._animate_sprites()
        if self.world.static["garbageCan"].current_frame_num == 0:
            self.world.static["garbageCan"].is_animating = False
        if not self.sparked:
            self._move_npcs(game_clock)

            # Events
            self.__check_sparks_collision()
        else:
            self._animate(self.world.NPCs["guy"], anim_once=False)
            self.credits.update_dt()
            if self.credits.dt.microseconds > 1.0 / self.credits.fps * 1000000:
                self.credits.update_credits()
            if self.credits.end:
                pygame.mixer.stop()
                raise utils.NextLevelException("room", 0)

        # Blitting
        self._blit(screen)

    def _blit(self, screen):
        screen.blit(self.world.bg, self.world.pos)
        for s in self.world.sprites:
            screen.blit(s.current_frame, s.pos)

        if self.sparked:
            screen.blit(self.credits.rect, (0, 0))
            [screen.blit(self.credits.texts[i], self.credits.texts_pos[i]) for i in xrange(len(self.credits.texts))]


    def __check_sparks_collision(self):
        # colliding with sparks
        if self.world.check_col(
                self.world.static["sparks"], self.world.NPCs["guy"]):
            self.world.NPCs["guy"].fps = 8
            self.world.NPCs["guy"].set_anim("E")
            self.sparked = True
            self.allow_move = False
