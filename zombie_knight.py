import pygame
import random

from settings import Settings
from tile import Tile
from ruby_maker import RubyMaker
from portal import Portal
from player import Player


class ZombieKnight:
    """The manin class for Zombie Knight game"""

    def __init__(self):
        """Initialize the game class attributes"""
        # Initialize pygame
        pygame.init()

        # Instantiate settings object
        self.settings = Settings()

        # Instantiate the player object
        self.player = Player

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

        # Create sprite groups
        # To draw the whole tiles on the screen at once
        self.main_tile_group = pygame.sprite.Group()
        # To check the collision between some tiles group(platform and player)
        self.platform_group = pygame.sprite.Group()

        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()

        self.zombie_group = pygame.sprite.Group()

        self.portal_group = pygame.sprite.Group()

        self.ruby_group = pygame.sprite.Group()

    # Create the tile map
    # / 0 -> no tile / 1 -> dirt / 2~5 -> platforms / 6 -> ruby maker / 7-8 -> portals / 9 -> player /
    # 23 rows and 40 columns
        tile_map = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        # Generate Tile objects from the tile map
        # Loop through the 23 lists (rows) in the tile map ( i moves us down the map )
        for i in range(len(tile_map)):
            # Loop through the 40 columns in a given list ( j moves us across the map )
            for j in range(len(tile_map[i])):
                # Dirt tile
                if tile_map[i][j] == 1:
                    Tile(j * 32, i * 32, 1, self.main_tile_group)
                elif tile_map[i][j] == 2:
                    Tile(j * 32, i * 32, 2, self.main_tile_group, self.platform_group)
                elif tile_map[i][j] == 3:
                    Tile(j * 32, i * 32, 3, self.main_tile_group, self.platform_group)
                elif tile_map[i][j] == 4:
                    Tile(j * 32, i * 32, 4, self.main_tile_group, self.platform_group)
                elif tile_map[i][j] == 5:
                    Tile(j * 32, i * 32, 5, self.main_tile_group, self.platform_group)
                # Ruby maker
                elif tile_map[i][j] == 6:
                    RubyMaker(j * 32, i * 32, self.main_tile_group)
                # Portals
                elif tile_map[i][j] == 7:
                    Portal(j * 32, i * 32, 'green', self.portal_group)
                elif tile_map[i][j] == 8:
                    Portal(j * 32, i * 32, 'purple', self.portal_group)
                # Player
                elif tile_map[i][j] == 9:
                    self.player = Player(j * 32 - 32, i * 32 + 32, self.platform_group, self.portal_group, self.bullet_group)
                    self.player_group.add(self.player)


    def run_game(self):
        """The main game loop"""
        while self.running:
            for event in pygame.event.get():
                # check if the user wants to quit
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    # If player wants to jump
                    if event.key == pygame.K_SPACE:
                        self.player.jump()

            # Update the screen
            self.update()


    def update(self):
        """Update and fill the screen"""
        # Blit the background
        self.screen.blit(self.bg_image, self.bg_rect)

        # Draw tiles and update ruby maker
        self.main_tile_group.update()
        self.main_tile_group.draw(self.screen)

        # Update and draw sprite groups
        self.portal_group.update()
        self.portal_group.draw(self.screen)

        self.player_group.update()
        self.player_group.draw(self.screen)

        # Update the screen and tick the clock
        pygame.display.flip()
        self.clock.tick(self.settings.FPS)



if __name__ == '__main__':
    zn = ZombieKnight()
    zn.run_game()

