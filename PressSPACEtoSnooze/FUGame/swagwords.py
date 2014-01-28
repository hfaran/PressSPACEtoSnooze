import pygame
from random import choice, randint

from FUGame.utils import utils


class SwagWord(object):

    def __init__(self, word, size=24):
        self._Y_BOUNDS = (200, 530)
        self._X_BOUNDS = (50, 500)
        self.word = word
        self.gen_new_rect()
        self.font = pygame.font.SysFont("comicsansms", size)
        self.fc = 0
        self.freq = randint(3, 10)
        self.color_fc = 0
        self.color_freq = randint(3, 10)
        self.gen_new_color()

    def gen_new_color(self):
        self.color = tuple([randint(0, 255) for i in xrange(3)])

    def gen_new_rect(self):
        self.rect = pygame.Rect(
            randint(*self._X_BOUNDS), randint(*self._Y_BOUNDS),
            400, 50)

    def draw(self, screen):
        self.fc = (self.fc + 1) % self.freq
        if self.fc < self.freq / 2:
            self.gen_new_color()

        # self.fc = (self.fc + 1) % self.freq
        # if self.fc < self.freq / 2:
        screen.blit(
                self.font.render(self.word, True, self.color), (self.rect.x, self.rect.y)
                )
        # utils.drawText(
        #     screen,
        #     self.word,
        #     self.color,
        #     self.rect,
        #     self.font,
        #     aa=True
        # )
