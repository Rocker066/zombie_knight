import pygame.key
from pygame.sprite import Sprite
from pygame import transform, image, mixer

from settings import Settings

class Player(Sprite):
    """A class the user can control"""

    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        """Initialize the player attribute"""
        super().__init__()

        # Initialize settings
        self.settings = Settings()
        self.vector = self.settings.vector

        # Set constant variables
        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        # Gravity
        self.VERTICAL_ACCELERATION = 0.8
        # Determines how high the player can jump
        self.STARTING_HEALTH = 100

        # Animation frames
        self.move_right_sprites = []
        self.move_left_sprites = []
        self.idle_right_sprites = []
        self.idle_left_sprites = []
        self.jump_right_sprites = []
        self.jump_left_sprites = []
        self.attack_right_sprites = []
        self.attack_left_sprites = []

        # Moving right animation list
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (1).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (2).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (3).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (4).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (5).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (6).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (7).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (8).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (9).png'), (64, 64))
        )
        self.move_right_sprites.append(transform.scale(
            image.load('assets/images/player/run/Run (10).png'), (64, 64))
        )

        # Moving left animation list
        for sprite in self.move_right_sprites:
            self.jump_left_sprites.append(transform.flip(sprite, True, False))

        # Idle right animation list
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (1).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (2).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (3).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (4).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (5).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (6).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (7).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (8).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (9).png'), (64, 64))
        )
        self.idle_right_sprites.append(transform.scale(
            image.load('assets/images/player/idle/Idle (10).png'), (64, 64))
        )

        # Idle left animation list
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(transform.flip(sprite, True, False))

        # jump right animation list
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (1).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (2).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (3).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (4).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (5).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (6).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (7).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (8).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (9).png'), (64, 64))
        )
        self.jump_right_sprites.append(transform.scale(
            image.load('assets/images/player/jump/Jump (10).png'), (64, 64))
        )

        # Jump left animation list
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(transform.flip(sprite, True, False))

        # Attack right animation list
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (1).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (2).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (3).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (4).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (5).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (6).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (7).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (8).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (9).png'), (64, 64))
        )
        self.attack_right_sprites.append(transform.scale(image.load(
            'assets/images/player/attack/Attack (10).png'), (64, 64))
        )

        # Attack left animation list
        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(transform.flip(sprite, True, False))

        # Load image and get rect
        self.current_sprite = 0
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        # Attach sprite groups
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group

        # Animation booleans ( in case of attack and fire )
        self.animate_jump = False
        self.animate_fire = False

        # Load sounds
        self.jump_sound =  mixer.Sound('assets/sounds/jump_sound.wav')
        self.slash_sound = mixer.Sound('assets/sounds/slash_sound.wav')
        self.portal_sound = mixer.Sound('assets/sounds/portal_sound.wav')
        self.hit_sound = mixer.Sound('assets/sounds/player_hit.wav')

        # Kinematics vectors
        self.position = self.vector(x, y)
        self.velocity = self.vector(0, 0)
        self.acceleration = self.vector(0, self.VERTICAL_ACCELERATION)

        # Set initial player values
        self.health = self.STARTING_HEALTH
        self.starting_x = x
        self.starting_y = y


    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()
        self.check_animations()


    def move(self):
        """Move the player"""
        # Set the acceleration vector
        self.acceleration = self.vector(0, self.VERTICAL_ACCELERATION)

        # if user is pressing a key, set the x-component of the acceleration to be non-zero
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION * -1
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION

        # Calculate new kinematics values: i.e (4, 1) + (2, 8) = (6, 9)
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + self.acceleration * 0.5

        # Update rect based on kinematic calculations and add wrap around movement
        if self.position.x < 0:
            self.position.x = self.settings.WIDTH
        elif self.position.x > self.settings.WIDTH:
            self.position.x = 0

        self.rect.bottomleft = self.position



    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        pass


    def check_animations(self):
        """Check to see if jump/fire animation should run"""
        pass


    def jump(self):
        """Jump upwards if on a platform"""
        pass


    def fire(self):
        """Fire a bullet from a sword"""
        pass


    def reset(self):
        """Reset the player's position"""
        pass


    def animate(self):
        """Animate the player's actions"""
        pass

