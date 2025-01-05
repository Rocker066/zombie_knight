import pygame.transform
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A projectile launched by the player"""

    def __init__(self, x, y, bullet_group, player):
        """Initialize the bullet attributes"""
        super().__init__()

        # Set constant variable
        self.VELOCITY = 20
        self.RANGE = 500

        # Load image and get the rect
        if player.velocity.x > 0:
            self.image = pygame.transform.scale(pygame.image.load('assets/images/player/slash.png'), (32, 32))
        else:
            self.image = pygame.transform.scale(pygame.transform.flip(
                pygame.image.load('assets/images/player/slash.png'), True, False), (32, 32))
            self.VELOCITY *= -1

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.starting_x = x

        bullet_group.add(self)


    def update(self):
        """Update the bullet"""
        # Move the bullet
        self.rect.x += self.VELOCITY

        # If the bullet has passed the range, kill it
        if abs(self.rect.x - self.starting_x) > self.RANGE:
            self.kill()