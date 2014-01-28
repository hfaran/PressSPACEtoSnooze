import pygame
from MyIsometricGame.utils import utils


class Tile(object):

    """Tile class"""

    def __init__(self, filename, x=0, y=0):
        self.image = utils.convert_white_to_transparent(
            pygame.image.load(
                "assets/tiles/{}.png".format(filename)
            )
        )
        self.mask = pygame.mask.from_surface(self.image)
        self._x = x
        self._y = y

    def get_pos(self):
        """Get position of Tile"""
        return self._x, self._y

    def set_pos(self, x, y):
        """Set position of Tile"""
        self._x = x
        self._y = y

    def point_collision(self, pos):
        """Test if `pos` collides with Tile

        :type  pos: (int, int)
        :param pos: Coordinates to test collision with Tile at
        :rtype: bool
        :returns: bool indicating if collision occurred
        """
        try:
            return self.mask.get_at(pos)
        except IndexError:
            return False
