import pygame.transform
from pygame.sprite import Sprite


class RubyMaker(Sprite):
    """A tile that's animated. A ruby will be generated here"""

    def __init__(self,x ,y, main_group):
        """Initialize the ruby maker's attributes"""
        super().__init__()

        # Animation frames
        self.ruby_sprites = []

        # Rotating animation
        self.ruby_sprites.append(pygame.transform.scale(
            pygame.image.load('assets/images/ruby/tile000.png'), (64, 64))
        )
        self.ruby_sprites.append(pygame.transform.scale(
            pygame.image.load('assets/images/ruby/tile001.png'), (64, 64))
        )
        self.ruby_sprites.append(pygame.transform.scale(
            pygame.image.load('assets/images/ruby/tile002.png'), (64, 64))
        )
        self.ruby_sprites.append(pygame.transform.scale(
            pygame.image.load('assets/images/ruby/tile003.png'), (64, 64))
        )
        self.ruby_sprites.append(pygame.transform.scale(
            pygame.image.load('assets/images/ruby/tile004.png'), (64, 64))
        )
        self.ruby_sprites.append(pygame.transform.scale(
            pygame.image.load('assets/images/ruby/tile005.png'), (64, 64))
        )
        self.ruby_sprites.append(pygame.transform.scale(
            pygame.image.load('assets/images/ruby/tile006.png'), (64, 64))
        )

        # Add to the main group for drawing purposes
        main_group.add(self)

        # Load image and get the rect
        self.current_sprite = 0
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)


    def animate(self, sprite_list, speed):
        """Animate the ruby maker"""
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0

        self.image = sprite_list[int(self.current_sprite)]


    def update(self):
        """Update the ruby maker"""
        self.animate(self.ruby_sprites, .25)