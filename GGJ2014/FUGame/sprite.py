import pygame
import os
from FUGame.utils import utils


class Sprite(object):
    """Sprite class
    """
    def __init__(self, filename, x, y):
        # self.image = utils.convert_white_to_transparent(
        #     pygame.image.load(
        #         "assets/sprites/{}/{}.png".format(filename, filename)
        #     )
        # )
        self.name = filename
        self._x = x
        self._y = y
        self.anims = self.load_frames()
        self.current_frame = list(self.anims.iteritems())[0][1][0]
        self.mask = pygame.mask.from_surface(self.current_frame)

    def get_pos(self):
        """Get position of Sprite"""
        return self._x, self._y

    def set_pos(self, x, y):
        """Set position of Sprite"""
        self._x = x
        self._y = y

    def load_frames(self):
        path = os.path.join("assets", "sprites", self.name)
        l = os.listdir(path)
        d = {
            folder_name: [pygame.image.load(
                os.path.join(path, folder_name, image)) for image in os.listdir(
                os.path.join(path, l))] for folder_name in l
        }
        # d = {}
        # for folder_name in l:
        #     for image in os.path.join(path, folder_name):
        #         d[folder_name]
        return d

    def point_collision(self, pos):
        """Test if `pos` collides with Sprite

        :type  pos: (int, int)
        :param pos: Coordinates to test collision with Sprite at
        :rtype: bool
        :returns: bool indicating if collision occurred
        """
        try:
            return self.mask.get_at(pos)
        except IndexError:
            return False
