from pygame.math import Vector2
from pygame import mixer
class Settings:
    """A class to store game settings"""

    def __init__(self):
        """Initialize the settings attributes"""
        # Set display values (tile siz is 32x32 so 1280/32 = 40 tiles wide, 736/32 = 23 tiles high)
        self.WIDTH = 1280
        self.HEIGHT = 738
        self.CAPTION = 'Zombie Knight'

        # Set FPS value
        self.FPS = 60

        # Set colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (25, 200, 25)

        # Use 2D vectors
        self.vector = Vector2

        # Load player and portal sounds
        self.jump_sound =  mixer.Sound('assets/sounds/jump_sound.wav')
        self.jump_sound.set_volume(.25)
        self.slash_sound = mixer.Sound('assets/sounds/slash_sound.wav')
        self.slash_sound.set_volume(.25)
        self.portal_sound = mixer.Sound('assets/sounds/portal_sound.wav')
        self.portal_sound.set_volume(.25)
        self.hit_sound = mixer.Sound('assets/sounds/player_hit.wav')
        self.hit_sound.set_volume(.25)

        # Load zombie sounds
        self.zombie_hit_sound = mixer.Sound('assets/sounds/zombie_hit.wav')
        self.zombie_hit_sound.set_volume(.25)
        self.zombie_kick_sound = mixer.Sound('assets/sounds/zombie_kick.wav')
        self.zombie_kick_sound.set_volume(.25)