import pygame
import os
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
        self.world.NPCs["guy"].set_anim("{}S".format(self.world.NPCs["guy"].direction))
        for s in self.world.static.values():
            if s.use_func and s.sprite_rect.colliderect(self.world.NPCs["guy"].sprite_rect):
                s.use_func()
                break
            elif s.name == "garbageCan" and s.sprite_rect.colliderect(self.world.NPCs["guy"].sprite_rect):
                s.is_animating = True
                break
            elif not self.coffee_spilt and s.name == "coffee" and s.sprite_rect.colliderect(
                    self.world.NPCs["guy"].sprite_rect):
                self.coffee_spilt = True
                self.door_open = True
                break
        if self.coffee_spilt and self.check_rival_collision():
            self.door_open = False
            self.world.NPCs["rival"].is_animating = True
        elif self.sparked:
            self.credits.speed += 5


    @property
    def event_map(self):
        _event_map = dict(self._move_event_map)
        _event_map[K_SPACE] = [self._use, ()]
        return _event_map


class Office(Level, EventHandlerMixin):
    def __init__(self, state=0):
        self.world = self.create_world()

        self.allow_move = True
        self.sparked = False
        self.credits = self.Credits()
        self.coffee_spilt = False
        self.door_open = False
        self.cmd_font = pygame.font.SysFont("verdana", 48)
        self.display_cmd = False
        self.cmd = "Press 'SPACE' to Apologize"
        self.door_rect = pygame.Rect(570, 215, 140, 20)

    def create_world(self):
        # Create objects
        chars = {
            "guy": Character(
                filename="main",
                x=420,
                y=240,
                z=0,
                col_pts=[],
                col_x_offset=50,
                col_y_offset=117,
                fps=10,
                speed=7
            ),
            "rival": Character(
                filename="rival",
                x=1070,
                y=215,
                z=55,
                col_pts=[],
                col_x_offset=0,
                col_y_offset=0,
                fps=10,
                speed=5
            )
        }
        chars["rival"].set_anim("W")
        chars["rival"].is_animating = True

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

            "coffee": Sprite(
                filename="coffee",
                x=900,
                y=150,
                z=-30,
                col_pts=[(85, 67), (117, 51), (135, 70)],
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
            ),

            "elevatorR": Sprite(
                filename="elevatorR",
                x=563,
                y=32,
                z=1,
                col_pts=[(40, 175)],
                col_x_offset=None,
                col_y_offset=None
            ),

            "elevatorL": Sprite(
                filename="elevatorL",
                x=638,
                y=32,
                z=1,
                col_pts=[(40, 175)],
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

        world.NPCs["guy"].set_anim("R")
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
            self.__check_chair_collision()
        else:
            self._animate(self.world.NPCs["guy"], anim_once=False)
            self.cmd = "Press 'SPACE' to Speed Up"
            self.display_cmd = True
            self.credits.update_dt()
            if self.credits.dt.microseconds > 1.0 / self.credits.fps * 1000000:
                self.credits.update_credits()
            if self.credits.end:
                pygame.mixer.stop()
                raise utils.NextLevelException("room", 0)

        if self.coffee_spilt:
            self._animate(self.world.static["coffee"], anim_once=True)

            if not self.world.static["coffee"].is_animating and self.door_open:
                if self.world.NPCs["rival"].is_animating:
                    self.world.NPCs["rival"].set_anim("A")
                    self.world.NPCs["rival"].is_animating = False
                    self.world.NPCs["rival"].nudge(-83, -45)
                    self.world.NPCs["rival"].set_z = 0
                self._animate(self.world.NPCs["rival"], anim_once=True)
            elif not self.door_open:
                if self.world.NPCs["rival"].is_animating and self.world.NPCs["rival"].current_anim == "A":
                    self.world.NPCs["rival"].set_anim("Z")
                    self.world.NPCs["rival"].is_animating = False
                elif self.world.NPCs["rival"].current_frame_num == len(self.world.NPCs["rival"].anims) - 1:
                    self.world.NPCs["rival"].set_anim("W")
                    self.world.NPCs["rival"].is_animating = True
                    self.world.NPCs["rival"].nudge(83, 45)
                    self.world.NPCs["rival"].set_z = 55
                self._animate(self.world.NPCs["rival"], anim_once=self.world.NPCs["rival"].is_animating)

            if self.door_open and self.__check_door_collision():
                pygame.mixer.stop()
                raise utils.NextLevelException("hills", 0)

            if self.door_open:
                if self.check_rival_collision():
                    self.display_cmd = True
                else:
                    self.display_cmd = False
            elif self.sparked:
                self.display_cmd = True
            else:
                self.display_cmd = False

        # Blitting
        self._blit(screen)

    def _blit(self, screen):
        screen.blit(self.world.bg, self.world.pos)
        for s in self.world.sprites:
            if not (s.name == "elevatorR" or s.name == "elevatorL") or not self.door_open:
                screen.blit(s.current_frame, s.pos)

        if self.sparked:
            screen.blit(self.credits.rect, (0, 0))
            [screen.blit(self.credits.texts[i], self.credits.texts_pos[i]) for i in xrange(len(self.credits.texts))]

        if self.display_cmd:
            screen.blit(self.cmd_font.render(self.cmd, True, FU_CMD_COLOR), FU_CMD_POS)


    def __check_sparks_collision(self):
        # colliding with sparks
        if self.world.check_col(
                self.world.static["sparks"], self.world.NPCs["guy"]):
            self.world.NPCs["guy"].fps = 8
            self.world.NPCs["guy"].set_anim("E")
            self.sparked = True
            self.allow_move = False

    def __check_chair_collision(self):
        # colliding with sparks
        if self.world.check_col(
                self.world.static["officeChairMain"], self.world.NPCs["guy"]):
            pygame.mixer.stop()
            if self.coffee_spilt:
                raise utils.NextLevelException("computer", 1)
            else:
                raise utils.NextLevelException("computer", 0)

    def __check_door_collision(self):
        return self.world.NPCs["guy"].sprite_rect.colliderect(self.door_rect)

    def check_rival_collision(self):
        return self.world.NPCs["guy"].col_rect.colliderect(self.world.NPCs["rival"].sprite_rect)
