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
