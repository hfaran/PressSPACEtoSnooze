import pygame
from MyIsometricGame.utils import utils


class Sprite(object):
    """Sprite class
    """
    def __init__(self):
        self.image = utils.convert_white_to_transparent(
            pygame.image.load(
                "assets/sprites/{}.png".format(filename)
            )
        )
        self.mask = pygame.mask.from_surface(self.image)
        self._x = x
        self._y = y

    def get_pos(self):
        """Get position of Sprite"""
        return self._x, self._y

    def set_pos(self, x, y):
        """Set position of Sprite"""
        self._x = x
        self._y = y

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
