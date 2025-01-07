import pygame.font
from settings import Settings
from zombie import Zombie
from player import Player

class Game:
    """A class to help manage gameplay"""

    def __init__(self, player, zombie_group, platform_group, portal_group, bullet_group, ruby_group, zk_game):
        """Initialize the game"""
        # Set constant variables
        self.STARTING_ROUND_TIME = 30
        self.STARTING_ZOMBIE_CREATION_TIME = 5

        # Instantiate settings
        self.settings = Settings()
        self.screen = zk_game.screen

        # Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME

        # Set fonts
        self.title_font = pygame.font.Font('assets/fonts/Poultrygeist.ttf', 48)
        self.HUD_font = pygame.font.Font('assets/fonts/Pixel.ttf', 24)

        # Attach groups and sprites
        self.player = player
        self.zombie_group = zombie_group
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group
        self.ruby_group = ruby_group


    def update(self):
        """Update the game"""
        # Update the round time every second
        self.frame_count += 1
        if self.frame_count % self.settings.FPS == 0:
            self.round_time -= 1
            self.frame_count = 0

        # Check for gameplay collisions
        self.check_collisions()

        # Add zombies if zombie creation time is met
        self.add_zombie()


    def draw(self):
        """Draw the game HUD"""
        # Set text
        score_text = self.HUD_font.render('Score:' + str(self.score), True, self.settings.WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, self.settings.HEIGHT - 50)

        health_text = self.HUD_font.render('Health:' + str(self.player.health), True, self.settings.WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, self.settings.HEIGHT - 25)

        title_text = self.title_font.render('Zombie Knight', True, self.settings.GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT - 25)

        round_text = self.HUD_font.render('Night: ' + str(self.round_number), True, self.settings.WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (self.settings.WIDTH - 10, self.settings.HEIGHT - 50)

        time_text = self.HUD_font.render('Sunrise In: ' + str(self.round_time), True, self.settings.WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (self.settings.WIDTH - 10, self.settings.HEIGHT - 25)

        # Draw the HUD
        self.screen.blit(score_text, score_rect)
        self.screen.blit(health_text, health_rect)
        self.screen.blit(title_text, title_rect)
        self.screen.blit(round_text, round_rect)
        self.screen.blit(time_text, time_rect)


    def add_zombie(self):
        """Add a zombie to the game"""
        # Check to add a zombie every second
        if self.frame_count % self.settings.FPS == 0:
            # Only add a zombie if zombie creation time has passed
            if self.round_time % self.zombie_creation_time == 0:
                zombie = Zombie(self.platform_group, self.portal_group, self.round_number, 5 + self.round_number)
                self.zombie_group.add(zombie)


    def check_collisions(self):
        """Check collisions that affect gameplay"""
        # See if any bullet in the bullet group hit a zombie in the zombie group
        collision_dict = pygame.sprite.groupcollide(self.bullet_group, self.zombie_group, True, False)
        if collision_dict:
            for zombies in collision_dict.values():
                for zombie in zombies:
                    self.settings.zombie_hit_sound.play()
                    zombie.is_dead = True
                    zombie.animate_death = True

        # See if a player stomped a dead zombie to finish it or collided with a live zombie to take damage
        collision_list = pygame.sprite.spritecollide(self.player, self.zombie_group, False)
        if collision_list:
            for zombie in collision_list:
                # the zombie is dead; stomp it
                if zombie.is_dead:
                    self.settings.zombie_kick_sound.play()
                    zombie.kill()
                    self.score += 25
                # The zombie is not dead; take damage
                else:
                    self.player.health -= 20
                    self.settings.hit_sound.play()
                    # Move the player to not continually take damage
                    self.player.position.x -= 256 * zombie.direction
                    self.player.rect.bottomleft = self.player.position


    def check_round_completion(self):
        """Check if the player survived a night"""
        pass


    def check_game_over(self):
        """Check to see if the player lost the game"""
        pass


    def start_new_round(self):
        """Start a new night"""
        pass


    def pause_game(self):
        """Pause the game"""
        pass


    def reset_game(self):
        """Reset the game"""
        pass