from pygame.sprite import Sprite


class Player(Sprite):
    """A class the user can control"""

    def __init__(self):
        """Initialize the player attribute"""
        super().__init__()
        pass


    def update(self):
        """Update the player"""
        pass


    def move(self):
        """Move the player"""
        pass


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

