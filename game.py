import pygame

from settings import Settings
from zombie import Zombie
from ruby import Ruby


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
        self.running = zk_game.running

        # Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME

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

        # Check round completion
        self.check_round_completion()

        # Check for game over
        self.check_game_over()


    def draw(self):
        """Draw the game HUD"""
        # Set text
        score_text = self.settings.HUD_font.render('Score:' + str(self.score), True, self.settings.WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, self.settings.HEIGHT - 50)

        health_text = self.settings.HUD_font.render('Health:' + str(self.player.health), True, self.settings.WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, self.settings.HEIGHT - 25)

        title_text = self.settings.title_font.render('Zombie Knight', True, self.settings.GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT - 25)

        round_text = self.settings.HUD_font.render('Night: ' + str(self.round_number), True, self.settings.WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (self.settings.WIDTH - 10, self.settings.HEIGHT - 50)

        time_text = self.settings.HUD_font.render('Sunrise In: ' + str(self.round_time), True, self.settings.WHITE)
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
                    ruby = Ruby(self.platform_group, self.portal_group)
                    self.ruby_group.add(ruby)
                    # Add to the speed of ruby velocity as level progresses
                    for ruby in self.ruby_group:
                        ruby.velocity.x = self.round_number + 2
                        # print(ruby.velocity)

                # The zombie is not dead; take damage
                else:
                    self.player.health -= 20
                    self.settings.hit_sound.play()
                    # Move the player to not continually take damage
                    self.player.position.x -= 256 * zombie.direction
                    self.player.rect.bottomleft = self.player.position

        # See if a player collided with a ruby
        if pygame.sprite.spritecollide(self.player, self.ruby_group, True):
            self.settings.ruby_pickup_sound.play()
            self.score += 10
            self.player.health += 10
            if self.player.health > self.player.STARTING_HEALTH:
                self.player.health = self.player.STARTING_HEALTH

        # See if a living zombie collided with a ruby
        for zombie in self.zombie_group:
            if not zombie.is_dead:
                if pygame.sprite.spritecollide(zombie, self.ruby_group, True):
                    self.settings.lost_ruby_sound.play()
                    zombie = Zombie(self.platform_group, self.portal_group, self.round_number, self.round_number + 5)
                    self.zombie_group.add(zombie)


    def check_round_completion(self):
        """Check if the player survived a night"""
        if self.round_time == 0:
            self.start_new_round()


    def check_game_over(self):
        """Check to see if the player lost the game"""
        if self.player.health <= 0:
            pygame.mixer.music.stop()
            self.pause_game('Game Over! Final Score: ' + str(self.score), 'Press Enter to play again')
            self.reset_game()


    def start_new_round(self):
        """Start a new night"""
        self.round_number += 1

        # Decrease zombie creation...more zombies
        if self.round_number < self.STARTING_ZOMBIE_CREATION_TIME:
            self.zombie_creation_time -= 1

        # Reset round values
        self.round_time = self.STARTING_ROUND_TIME

        self.zombie_group.empty()
        self.ruby_group.empty()
        self.bullet_group.empty()

        self.player.reset()

        self.pause_game('You Survived the night!', 'Press ENTER to continue...')


    def pause_game(self, main_text, sub_text):
        """Pause the game"""
        pygame.mixer.music.pause()

        # Create main pause text
        main_text = self.settings.title_font.render(main_text, True, self.settings.GREEN)
        main_rect = main_text.get_rect()
        main_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2)

        # Create sub pause text
        sub_text = self.settings.title_font.render(sub_text, True, self.settings.WHITE)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (self.settings.WIDTH // 2, self.settings.HEIGHT // 2 + 64)

        # Display the pause text
        self.screen.fill(self.settings.BLACK)
        self.screen.blit(main_text, main_rect)
        self.screen.blit(sub_text, sub_rect)
        pygame.display.update()

        # Pause the game until player hits enter
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # User wants to continue
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                        pygame.mixer.music.unpause()
                # user wants to quit
                if event.type == pygame.QUIT:
                    is_paused = False
                    pygame.mixer.music.stop()


    def reset_game(self):
        """Reset the game"""
        # Reset game values
        self.score = 0
        self.round_number = 1
        self.round_time = self.STARTING_ROUND_TIME
        self.zombie_creation_time = self.STARTING_ZOMBIE_CREATION_TIME

        # Reset the player
        self.player.health = self.player.STARTING_HEALTH
        self.player.reset()

        # Empty sprite groups
        self.zombie_group.empty()
        self.ruby_group.empty()
        self.bullet_group.empty()

        # Replay the music
        pygame.mixer.music.play()
