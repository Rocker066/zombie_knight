import pygame
import random

from settings import Settings


class ZombieKnight:
    """The manin class for Zombie Knight game"""

    def __init__(self):
        """Initialize the game class attributes"""
        # Initialize pygame
        pygame.init()

        # Instantiate settings object
        self.settings = Settings()

        # Use 2D vectors
        self.vector = pygame.math.Vector2

        # Set the state of the game
        self.running = True

        # Set display surface
        self.screen = pygame.display.set_mode((self.settings.WIDTH, self.settings.HEIGHT))
        pygame.display.set_caption(self.settings.CAPTION)

        # Load in a background image
        self.bg_image = pygame.transform.scale(pygame.image.load('assets/images/background.png'),(1280, 736))
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.topleft = (0, 0)

        # Set the clock
        self.clock = pygame.time.Clock()


    def run_game(self):
        """The main game loop"""
        while self.running:
            for event in pygame.event.get():
                # check if the user wants to quit
                if event.type == pygame.QUIT:
                    self.running = False

            # Update the screen
            self.update()


    def update(self):
        """Update and fill the screen"""
        # Blit the background
        self.screen.blit(self.bg_image, self.bg_rect)

        # Update the screen and tick the clock
        pygame.display.flip()
        self.clock.tick(self.settings.FPS)



if __name__ == '__main__':
    zn = ZombieKnight()
    zn.run_game()

