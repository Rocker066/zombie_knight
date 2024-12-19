from pygame.sprite import Sprite


class Ruby(Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self):
        """Initialize the ruby's attributes"""
        super().__init__()


    def update(self):
        """Update the ruby"""
        pass


    def move(self):
        """Move the ruby"""
        pass
    
    
    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        pass


    def animate(self):
        """Animate the ruby"""
        pass