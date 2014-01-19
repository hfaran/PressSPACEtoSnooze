import pygame
from pygame.locals import *
from MyIsometricGame.utils import utils
from MyIsometricGame.tile import Tile

from random import randint, choice
from itertools import chain


def generate_floor(numx, numy):
    """Create a tiled floor of size numx, numy"""
    __colors = ["pink", "green", "purple", "orange"]
    def getx(x,y,w,h):
        return int((x+y)*w/2.0)
    def gety(x,y,w,h):
        return int((numy+x-y)*h/2.0)

    l = []
    for x in xrange(numx):
        for y in xrange(numy):
            t = Tile(choice(__colors))
            width, height = t.image.get_size()
            t.set_pos(getx(x,y,width,height), gety(x,y,width,height))
            l.append(t)
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

    # Add tiles
    screen.blit(bg, (0,)*2)
    for t in tiles:
        print t.get_pos()
        screen.blit(t.image, t.get_pos())
    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos
                print x,y
                for n, t in enumerate(tiles):
                    if t.point_collision((x-t._x,y-t._y)):
                        print n
                        break


if __name__ == '__main__':
    main()
