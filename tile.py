import pygame.image
from pygame.sprite import Sprite


class Tile(Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, x, y, image_int, main_group, sub_group=''):
        """Initialize the tile attributes"""
        super().__init__()

        # Load in the correct image and add it to the correct sub_group
        # Dirt Tiles
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load('assets/images/tiles/Tile (1).png'), (32, 32))
        # Platform Tiles
        elif image_int == 2:
            self.image = pygame.transform.scale(pygame.image.load('assets/images/tiles/Tile (2).png'), (32, 32))
            sub_group.add(self)
        elif image_int == 3:
            self.image = pygame.transform.scale(pygame.image.load('assets/images/tiles/Tile (3).png'), (32, 32))
            sub_group.add(self)
        elif image_int == 4:
            self.image = pygame.transform.scale(pygame.image.load('assets/images/tiles/Tile (4).png'), (32, 32))
            sub_group.add(self)
        elif image_int == 5:
            self.image = pygame.transform.scale(pygame.image.load('assets/images/tiles/Tile (5).png'), (32, 32))
            sub_group.add(self)

        # Add every tile to the main group
        main_group.add(self)

        # Get the rect of the image and position within the grid
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

