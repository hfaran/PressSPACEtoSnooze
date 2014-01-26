import pygame
from random import choice, randint

from FUGame.utils import utils


class SwagWord(object):

    def __init__(self, word):
        self._Y_BOUNDS = (200, 530)
        self._X_BOUNDS = (50, 500)
        self.word = word
        self.gen_new_rect()
        self.font = pygame.font.SysFont("comicsansms", 24)
        self.fc = 0
        self.freq = randint(3, 10)

    def gen_new_rect(self):
        self.rect = pygame.Rect(
            randint(*self._X_BOUNDS), randint(*self._Y_BOUNDS),
            150, 50)

    def draw(self, screen):
        self.fc = (self.fc + 1) % self.freq
        if self.fc < self.freq / 2:
            utils.drawText(
                screen,
                self.word,
                tuple([randint(0, 255) for i in xrange(3)]),
                self.rect,
                self.font,
                aa=True
            )
