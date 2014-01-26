import pygame
import os
from pygame.locals import *

from FUGame.character import Character, Sprite
from FUGame.world import World
from FUGame.constants import *
from FUGame.utils import utils
from FUGame.levels.level import Level, BaseEventHandlerMixin

from random import randint
from datetime import datetime


class EventHandlerMixin(BaseEventHandlerMixin):
    def _move_character(self, direction):
        if self.allow_move:
            self.guy.is_moving = True
            self.guy.direction = direction
            return True

    def _use(self):
        if self.display_cmd and not self.game_over:
            self.display_cmd = False
            self.snooze_time = datetime.now()
            self.guy.set_anim("SNZ")
            # Button
            self.world.static["button"].set_anim("D")
            self.world.static["button"].nudge(0, 5)
            if self.alarm_on:
                self.alarm.stop()
                self.alarm_on = False
                self.snooze_count += 1
            return True
        elif self.game_over:
            self.credits.speed += 5
        else:
            self.guy.set_anim("{}S".format(self.guy.direction))
            for s in self.world.static.values():
                if s.use_func and s.sprite_rect.colliderect(
                        self.guy.sprite_rect):
                    s.use_func()
                    break
                elif s.name == "chair" and s.sprite_rect.colliderect(
                        self.guy.sprite_rect):
                    if self.guy.pos[1] > s.pos[1] and s.pos[1] - 50 > 200:
                        s.nudge(0, -50)
                    elif self.guy.pos[1] < s.pos[1] and s.pos[1] - 50 < 330:
                        s.nudge(0, 50)
                    break
                elif s.name == "cell" and s.sprite_rect.colliderect(
                        self.guy.sprite_rect):
                    s.set_pos(-500, -500)

    def _stop_snooze(self):
        if self.guy.current_anim == "SNZ":
            self.guy.set_anim("L")
            # Button
            self.world.static["button"].set_anim("U")
            self.world.static["button"].nudge(0, -5)
            return True

    @property
    def event_map(self):
        _event_map = dict(self._move_event_map)
        _event_map[K_SPACE] = [self._use, ()]
        return _event_map

    @property
    def false_event_map(self):
        _event_map = {
            K_SPACE: [self._stop_snooze, ()]
        }
        return _event_map


class Room(Level, EventHandlerMixin):
    cloud_min_x = 200
    cloud_max_x = 300
    cloud_min_y = 0
    cloud_max_y = 150

    def __init__(self, state=0):
        self.world = self.create_world()
        self.guy = self.world.NPCs["guy"]
        self.state = state
        self.clock_font = pygame.font.SysFont("comicsansms", 16)
        self.cmd_font = pygame.font.SysFont("verdana", 48)
        self.cmd = "Press 'SPACE' to Snooze"
        self.display_cmd = False
        self.allow_move = False
        self.is_waking = False
        self.snooze_length = 3  # TODO MAKE 9 DEV: 3
        self.msg_count = 0
        self.phone = self.Phone()
        self.game_over = False
        self.credits = self.Credits()
        self.snooze_count = 0
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join(FU_APATH, "music", "bedroomfinal.wav"))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()
        pygame.mixer.music.queue(os.path.join(FU_APATH, "music", "bedroomfinal.wav"))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
        self.ambience = pygame.mixer.Sound(os.path.join(FU_APATH, "soundFX", "room_amb.wav"))
        self.ambience.set_volume(0.25)
        self.ambience.play(-1)
        self.vibrate = pygame.mixer.Sound(os.path.join(FU_APATH, "soundFX", "vibrate.wav"))
        self.alarm = pygame.mixer.Sound(os.path.join(FU_APATH, "soundFX", "alarm.wav"))
        self.alarm_on = False

        self.sky = Sprite(
            filename="sky",
            x=515,
            y=40,
            z=0,
            col_pts=[],
            col_x_offset=None,
            col_y_offset=None
        )

        self.clouds = [
            Sprite(
                filename="cloud" + str(i),
                x=randint(470, 800),
                y=randint(self.cloud_min_y, self.cloud_max_y),
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None,
                fps=10
            ) for i in xrange(1, 5)
        ]

        self.door_rect = pygame.Rect(75, 365, 100, 130)

        self.snooze_time = datetime.now()
        self.start_time = datetime.now()
        self.game_time = datetime.now() - self.start_time
        self.clock_time = self.seconds_to_time(self.game_time.total_seconds())
        self.clock_text = self.clock_font.render(
            self.clock_time, True, (0, 255, 0))

        if state in [1]:
            self.guy.set_pos(425, self.guy.pos[1])
            self.guy.set_anim("R")
            self.guy.direction = "R"
            self.guy.is_animating = False
            self.guy.is_moving = True

    def seconds_to_time(self, secs):
        secs = secs + 51 + 5 * 60
        secs += 12*60-51 if self.state in [1] else 0
        hours = int(secs / 60)
        mins = int(secs % 60)

        return "{}:{}".format(hours, str(mins).zfill(2))

    def create_world(self):
        # Create objects
        chars = {
            "guy": Character(
                filename="main",
                x=525,
                y=190,
                z=0,
                col_pts=[],
                col_x_offset=50,
                col_y_offset=117,
                fps=4,
                speed=7
            ),
        }

        statics = {
            "desk": Sprite(
                filename="desk",
                x=1075,
                y=210,
                z=0,
                col_pts=[(
                             4, 61), (
                             17, 120), (
                             27, 171), (
                             40, 221), (
                             56, 294), (69, 56), (120, 293), (182, 293),
                         (131, 56)],
                col_x_offset=None,
                col_y_offset=None
            ),
            "chair": Sprite(
                filename="chair",
                x=950,
                y=330,
                z=0,
                col_pts=[(5, 80), (36, 112), (75, 120), (110, 105),
                         (110, 70), (85, 30), (25, 55), (50, 30)],
                col_x_offset=None,
                col_y_offset=None
            ),
            "sideTable": Sprite(
                filename="sideTable",
                x=420,
                y=169,
                z=0,
                col_pts=[(20, 110), (65, 110), (115, 110),
                         (105, 40), (20, 40), (15, 55)],
                col_x_offset=None,
                col_y_offset=None
            ),
            "cell": Sprite(
                filename="cell",
                x=1125,
                y=360,
                z=30,
                fps=15,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),
            "alarmClock": Sprite(
                filename="alarmClock",
                x=450,
                y=200,
                z=50,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),
            "button": Sprite(
                filename="button",
                x=462,
                y=190,
                z=95,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),
            "bed": Sprite(
                filename="bed",
                x=545,
                y=170,
                z=0,
                col_pts=[(
                             30, 310), (
                             80, 310), (
                             130, 310), (
                             180, 310), (
                             230, 310), (250, 310), (5, 265), (65, 265),
                         (125, 265), (185, 265), (245,
                                                  265), (
                             270, 265), (
                             0, 100), (65, 100),
                         (125, 100), (185, 100), (245, 100), (270, 100), (10, 60), (235, 60)],
                col_x_offset=15,
                col_y_offset=15
            ),
            "blanket": Sprite(
                filename="blanket",
                x=535,
                y=240,
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),
            "pillows": Sprite(
                filename="pillows",
                x=545,
                y=160,
                z=0,
                col_pts=[],
                col_x_offset=None,
                col_y_offset=None
            ),
            "door": Sprite(
                filename="door",
                x=40,
                y=60,
                z=0,
                col_pts=[(70, 325), (125, 300), (180, 275)],
                col_x_offset=None,
                col_y_offset=None
            )
        }

        world = World(
            level_id="room",
            bg_filename="room_bg",
            static=statics,
            NPCs=chars,
            col_pts=[(
                         49, 630), (
                         63, 555), (
                         75, 500), (
                         48, 464), (
                         95, 370), (65, 305), (49, 267), (115, 280),
                     (130, 210), (195, 210), (260, 210), (325, 210), (390,
                                                                      210), (
                         455, 210), (
                         520, 210), (
                         585, 210),
                     (650, 210), (715, 210), (780, 210), (845, 210), (910,
                                                                      210), (
                         975, 210), (
                         1040, 210), (
                         1105, 210),
                     (1170, 210), (1200, 210), (1210, 265), (1220, 305), (1255, 500), (1270, 560), (1280, 630)],
            x=0,
            y=0
        )

        world.NPCs["guy"].set_anim("S")
        world.NPCs["guy"].is_animating = True

        world.static["pillows"].set_z(world.static["bed"].z_index + 1
                                      - world.static["pillows"].pos[1]
                                      - world.static["pillows"].current_frame.get_height())

        return world

    def handle_events(self, event):
        truthy_res = False
        falsy_res = False
        keys = pygame.key.get_pressed()

        for key, l in self.false_event_map.iteritems():
            func, args = l
            if not keys[key]:
                falsy_res = bool(func(*args))

        for key, l in self.event_map.iteritems():
            func, args = l
            if keys[key]:
                truthy_res = bool(func(*args))

        if not truthy_res and self.state in [0]:
            self.guy.is_moving = False
        return truthy_res or falsy_res

    def char_in_bed(self, sprite_rect):
        bed_rect = self.world.static["bed"].col_image.get_rect()
        bed_rect.x, bed_rect.y = self.world.static["bed"].col_pos

        if bed_rect.colliderect(sprite_rect):
            return True

    def _wake_character(self):
        self.guy.is_moving = True
        self.guy.direction = "L"

    def update_loop(self, screen, game_clock):
        """"""
        # STATE 1 #
        if self.state in [1]:
            if not self.game_over:
                self._animate_sprites()
                self._move_npcs(game_clock)
            if self.guy.pos[0] > 525:
                self.guy.is_moving = False
                self.game_over = True

        self.game_time = datetime.now() - self.start_time
        self.clock_time = self.seconds_to_time(self.game_time.total_seconds())
        self.clock_text = self.clock_font.render(
            self.clock_time, True, FU_CMD_COLOR)

        self.update_clouds()

        # STATE 0 #
        if self.state in [0]:
            if not self.game_over:
                self._animate_sprites()
                self._move_npcs(game_clock)

                if self.door_rect.colliderect(self.guy.col_rect):
                    pygame.mixer.stop()
                    raise utils.NextLevelException("computer", 0)

                if not self.allow_move:
                    if self.guy.pos[0] < 425:
                        self.allow_move = True
                        self.guy.is_moving = False
                    elif self.is_waking:
                        self._wake_character()
                        self.guy.is_animating = False
                        self.guy.fps = 10
                    elif (datetime.now() - self.snooze_time).total_seconds() >= self.snooze_length * 2:
                        self.display_cmd = False
                        self.is_waking = True
                        self.guy.set_anim("L")
                        self.alarm.stop()
                        self.alarm_on = False
                    elif (datetime.now() - self.snooze_time).total_seconds() >= self.snooze_length:
                        self._stop_snooze()
                        self.guy.is_animating = False
                        self.guy.set_anim("W")
                        self.display_cmd = True
                        self.cmd = "Press 'SPACE' to Snooze"
                        if not self.alarm_on:
                            self.alarm.play(999)
                            self.alarm_on = True

                if 0 <= (self.game_time.total_seconds() + 51) % 30 <= 5 and \
                        self.game_time.total_seconds() > 9:  # TODO make 39 DEV: 9
                    self._animate(self.world.static["cell"])

                    if not self.phone.up:
                        if self.msg_count == 0:
                            self.phone.show_phone("Reminder Alarm - work @ 8am", "Iris")
                        elif self.msg_count == 1:
                            self.phone.show_phone("Reminder Reminder Alarm - work @ 8am", "Iris")
                        elif self.msg_count == 2:
                            self.phone.show_phone("Txt 59095 to donat $5 to http://spam.notascam.org", "Nigerian Prince")
                        elif self.msg_count == 3:
                            self.phone.show_phone("You able to get the weekend off? :)", "Jamie")
                        elif self.msg_count == 4:
                            self.phone.show_phone("You're late. Be here soon.", "JerkBossFace")
                        elif self.msg_count == 5:
                            self.phone.show_phone("Where are you?? GET HERE", "JerkBossFace")
                        elif self.msg_count == 6:
                            self.phone.show_phone("Your e-bill is ready. Sign in to view.", "Robelus Mobile")
                        elif self.msg_count == 7:
                            self.phone.show_phone("Don't bother. You're FIRED!", "JerkBossFace")
                            self.game_over = True
                        self.msg_count += 1
                        self.vibrate.play(999, maxtime=5000)


                else:
                    self.world.static["cell"].set_anim("I")
                    self.phone.hide_phone()

        self.phone.update_phone()

        if self.char_in_bed(self.guy.col_rect):
            self.guy.set_z(self.world.static["bed"].z_index + 1
                                         - self.guy.pos[1]
                                         - self.guy.current_frame.get_height())
        else:
            self.guy.set_z(0)

        if self.game_over:
            self.cmd = "Press 'SPACE' to Speed Up"
            self.display_cmd = True
            self.credits.update_dt()
            if self.credits.dt.microseconds > 1.0 / self.credits.fps * 1000000:
                self.credits.update_credits()
            if self.credits.end:
                pygame.mixer.stop()
                raise utils.NextLevelException("room", 0)

        # CALL TO self._blit #
        self._blit(screen)

    def _blit(self, screen):
        # Blitting
        screen.blit(self.sky.current_frame, self.sky.pos)

        for c in sorted(self.clouds, key=lambda x: x.pos[1]):
            screen.blit(c.current_frame, c.pos)

        screen.blit(self.world.bg, self.world.pos)

        for s in self.world.sprites:
            screen.blit(s.current_frame, s.pos)
            if s.name == "alarmClock":
                screen.blit(self.clock_text, (s.pos[0] + 25, s.pos[1] + 20))

        screen.blit(self.phone.image, self.phone.pos)
        screen.blit(self.phone.sender_font.render(self.phone.sender, True, (200, 200, 200)), self.phone.sender_pos)
        utils.drawText(screen, self.phone.message, (50, 50, 50),
                       pygame.Rect(self.phone.msg_pos[0], self.phone.msg_pos[1], 155, 90),
                       self.phone.msg_font, aa=True)

        screen.blit(pygame.font.SysFont("comicsansms", 16).render(str(self.snooze_count), True, (255, 255, 255)), (FU_WIDTH/2, 10))

        s = pygame.Surface((self.phone.image.get_width(), FU_HEIGHT - 630))
        s.fill((0, 0, 0))
        screen.blit(s, (self.phone.pos[0], 630))

        if self.game_over:
            screen.blit(self.credits.rect, (0, 0))
            [screen.blit(self.credits.texts[i], self.credits.texts_pos[i]) for i in xrange(len(self.credits.texts))]

        if self.display_cmd:
            screen.blit(
                self.cmd_font.render(self.cmd, True, FU_CMD_COLOR), FU_CMD_POS)

    def update_clouds(self):
        for c in self.clouds:
            if c.pos[0] > 880:
                c.set_pos(randint(self.cloud_min_x, self.cloud_max_x),
                          randint(self.cloud_min_y, self.cloud_max_y))
            else:
                c.set_pos(c.pos[0] + randint(1, 4), c.pos[1])

    class Phone:
        def __init__(self):
            self.image = pygame.image.load(
                os.path.join(FU_APATH, "UI", "phone_message.png")
            )
            self.pos = (1300 - self.image.get_width(), 630)
            self.message = ""
            self.sender = ""
            self.move_up = False
            self.move_down = False
            self.up = False
            self.sender_font = pygame.font.SysFont("verdana", 20)
            self.msg_font = pygame.font.SysFont("helvetica", 18)

        def show_phone(self, msg, sender):
            self.move_up = True
            self.message = msg
            self.sender = sender

        def hide_phone(self):
            self.move_down = True

        @property
        def sender_pos(self):
            return self.pos[0]+20, self.pos[1]+83

        @property
        def msg_pos(self):
            return self.pos[0]+45, self.pos[1]+210

        def update_phone(self):
            if self.move_up:
                if self.pos[1] > (630 - self.image.get_height()):
                    self.pos = (self.pos[0], self.pos[1] - 30)
                    self.up = True
                else:
                    self.pos = (self.pos[0], (630 - self.image.get_height()))
                    self.move_up = False
            elif self.move_down:
                if self.pos[1] < 630:
                    self.pos = (self.pos[0], self.pos[1] + 30)
                else:
                    self.pos = (self.pos[0], 630)
                    self.move_down = False
                    self.up = False
