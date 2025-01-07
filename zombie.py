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
        self.move()
        self.check_collisions()
        self.check_animations()

        # Determine when the zombie should rise from the dead
        if self.is_dead:
            self.frame_count += 1
            if self.frame_count % self.settings.FPS == 0:
                self.round_time += 1
                if self.round_time == self.RISE_TIME:
                    self.animate_rise = True
                    # When the zombie died, the image was kept as the last image
                    # When it rises, we want to start at index 0 of our rise_sprite lists
                    self.current_sprite = 0


    def move(self):
        """Move the zombie"""
        if not self.is_dead:
            if self.direction == -1:
                self.animate(self.walk_left_sprites, .5)
            else:
                self.animate(self.walk_right_sprites, .5)

            # We don't need to update the acceleration vector because it never changes here
            # Calculate new kinematics values
            self.velocity += self.acceleration
            self.position += self.velocity + 0.5 * self.acceleration

            # Update rect based on kinematic calculations and add wrap around movement
            if self.position.x < 0:
                self.position.x = self.settings.WIDTH
            elif self.position.x > self.settings.WIDTH:
                self.position.x = 0

            self.rect.bottomleft = self.position


    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        # Collision check between zombie and platforms when falling
        collided_platforms = pygame.sprite.spritecollide(self, self.platform_group, False)
        if collided_platforms:
            self.position.y = collided_platforms[0].rect.top + 1
            self.velocity.y = 0

        # Collision check for portals
        if pygame.sprite.spritecollide(self, self.portal_group, False):
            self.settings.portal_sound.play()
            # Determine which portal you are moving to
            # Left and right
            if self.position.x > self.settings.WIDTH // 2:
                self.position.x = 86
            else:
                self.position.x = self.settings.WIDTH - 150

            # Top and bottom
            if self.position.y > self.settings.HEIGHT // 2:
                self.position.y = 64
            else:
                self.position.y = self.settings.HEIGHT - 132

            self.rect.bottomleft = self.position


    def check_animations(self):
        """Check to see if death/rise animation should run"""
        # Animate the zombie death
        if self.animate_death:
            if self.direction == 1:
                self.animate(self.die_right_sprites, .095)
            else:
                self.animate(self.die_left_sprites, .095)

        # Animate the zombie rise
        if self.direction == 1:
            self.animate(self.rise_right_sprites, .095)
        else:
            self.animate(self.rise_left_sprites, .095)


    def animate(self, sprite_list, speed):
        """Animate the zombie's actions"""
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
            # End the death animation
            if self.animate_death:
                self.current_sprite = len(sprite_list) - 1
                self.animate_death = False
            # End the rise animation
            if self.animate_rise:
                self.animate_rise = False
                self.is_dead = False
                self.frame_count = 0
                self.round_time = 0

        self.image = sprite_list[int(self.current_sprite)]

