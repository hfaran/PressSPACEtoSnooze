import pygame
from pygame.locals import *
from MyIsometricGame.utils import utils
from MyIsometricGame.tile import Tile

from random import randint, choice
from itertools import chain


COLORS = ["pink", "green", "purple", "orange"]
def generate_floor(numx, numy):
    def getx(x,y,w,h):
        return int((x+y)*w/2.0)
    def gety(x,y,w,h):
        return int((numy+x-y)*h/2.0)
    l = []
    for x in xrange(numx):
        for y in xrange(numy):
            t = Tile(choice(COLORS))
            width, height = t.image.get_size()
            t.set_pos(getx(x,y,width,height), gety(x,y,width,height))
            l.append(t)
    #return [[Tile(choice(COLORS), getx(x,y), gety(x,y)) for x in xrange(numx)] for y in xrange(y)])
    return l

def main():
    # Init screen
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('MyIsometricGame')

    # Load images
    tiles = generate_floor(5, 5)

    # Fill background
    bg = pygame.Surface(screen.get_size())
    bg.fill((100,)*3)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos
                print x,y

        screen.blit(bg, (0,)*2)
        for t in tiles:
            print t.get_pos()
            screen.blit(t.image, t.get_pos())



        pygame.display.flip()

if __name__ == '__main__':
    main()
