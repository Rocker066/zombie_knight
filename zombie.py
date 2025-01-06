import random
import pygame.transform
from pygame.sprite import Sprite

from settings import Settings


class Zombie(Sprite):
    """An enemy class that moves across the screen"""

    def __init__(self, platform_group, portal_group, min_speed, max_speed):
        """Initialize the zombie attribute"""
        super().__init__()

        # Initialize settings
        self.settings = Settings()

        # Set constant variables
        # Gravity
        self.VERTICAL_ACCELERATION = 3
        self.RISE_TIME = 2

        # Animation Frames
        self.walk_right_sprites = []
        self.walk_left_sprites = []
        self.die_right_sprites = []
        self.die_left_sprites = []
        self.rise_right_sprites = []
        self.rise_left_sprites = []

        # Male(0) and female(1) zombies
        gender = random.randint(0, 1)

        if gender == 0:
            # Walking right
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (1).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (2).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (3).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (4).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (5).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (6).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (7).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (8).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (9).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/walk/Walk (10).png'), (64, 64)))

            # Walking left
            for sprite in self.walk_right_sprites:
                self.walk_left_sprites.append(pygame.transform.flip(sprite, True, False))

            # Dying right
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (1).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (2).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (3).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (4).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (5).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (6).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (7).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (8).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (9).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (10).png'), (64, 64)))

            # Dying left
            for sprite in self.die_right_sprites:
                self.die_left_sprites.append(pygame.transform.flip(sprite, True, False))

            # Rising right
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (10).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (9).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (8).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (7).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (6).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (5).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (4).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (3).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (2).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/boy/dead/Dead (1).png'), (64, 64)))

            # Rising left
            for sprite in self.rise_right_sprites:
                self.rise_left_sprites.append(pygame.transform.flip(sprite, True, False))

        else:
            # Walking right
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (1).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (2).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (3).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (4).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (5).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (6).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (7).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (8).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (9).png'), (64, 64)))
            self.walk_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/walk/Walk (10).png'), (64, 64)))

            # Walking left
            for sprite in self.walk_right_sprites:
                self.walk_left_sprites.append(pygame.transform.flip(sprite, True, False))

            # Dying right
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (1).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (2).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (3).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (4).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (5).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (6).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (7).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (8).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (9).png'), (64, 64)))
            self.die_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (10).png'), (64, 64)))

            # Dying left
            for sprite in self.die_right_sprites:
                self.die_left_sprites.append(pygame.transform.flip(sprite, True, False))

            # Rising right
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (10).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (9).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (8).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (7).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (6).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (5).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (4).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (3).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (2).png'), (64, 64)))
            self.rise_right_sprites.append(pygame.transform.scale(
                pygame.image.load('assets/images/zombie/girl/dead/Dead (1).png'), (64, 64)))

            # Rising left
            for sprite in self.rise_right_sprites:
                self.rise_left_sprites.append(pygame.transform.flip(sprite, True, False))

        # Load an image and get the rect
        # Set direction => (-1) left, (1) right
        self.direction = random.choice([-1, 1])

        self.current_sprite = 0

        if self.direction == -1:
            self.image = self.walk_left_sprites[self.current_sprite]
        else:
            self.image = self.walk_right_sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (random.randint(100, self.settings.WIDTH - 100), -100 )

        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group

        # Animation booleans
        self.animate_death = False
        self.animate_rise = False

        # Load sounds
        self.hit_sound = pygame.mixer.Sound('assets/sounds/zombie_hit.wav')
        self.kick_sound = pygame.mixer.Sound('assets/sounds/zombie_kick.wav')
        self.portal_sound = pygame.mixer.Sound('assets/sounds/portal_sound.wav')

        # Kinematics vectors
        self.position = self.settings.vector(self.rect.x, self.rect.y)
        self.velocity = self.settings.vector(self.direction * random.randint(min_speed, max_speed), 0)
        self.acceleration = self.settings.vector(0, self.VERTICAL_ACCELERATION)

        # Initial zombie values
        self.is_dead = False
        self.round_time = 0
        self.frame_count = 0


    def update(self):
        """Update the zombie"""
        pass


    def move(self):
        """Move the zombie"""
        pass


    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        pass


    def check_animations(self):
        """Check to see if death/rise animation should run"""
        pass


    def animate(self):
        """Animate the zombie's actions"""
        pass

