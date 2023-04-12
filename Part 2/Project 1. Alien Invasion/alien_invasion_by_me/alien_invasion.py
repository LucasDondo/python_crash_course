import sys
from time import sleep

import pygame
import json

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from play_button import PlayButton
from rocket import Rocket
from bullet import Bullet
from alien import Alien

class AlienInvasion():
    ''' Overall class to to manage game assets and behavior. '''

    def __init__(self):
        ''' Initialize the game, and create game resources. '''

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        # Create an instance to store game statistics and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.rocket = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Create the play button.
        self.play_button = PlayButton(self, 'Play')

        # Set the background color.
        self.bg_color = self.settings.bg_color

    def run_game(self):
        ''' Start the main loop for the game. '''

        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()

            if self.stats.game_active:
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        ''' Respond to keypresses and mouse events. '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._exit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button_clicked(mouse_pos)

    def _check_keydown_events(self, event):
        ''' Respond to keypresses. '''

        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            self._exit_game()
        elif event.key == pygame.K_SPACE:
            self._check_shoot_bullet()
        elif event.key == pygame.K_p:
            self._check_play_button_keys()

    def _check_keyup_events(self, event):
        ''' Respond to key releases. '''

        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

    def _check_play_button_clicked(self, mouse_pos):
        ''' Start new game when the player clicks Play. '''
    
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if play_button_clicked and not self.stats.game_active:
            self._start_game()
    
    def _check_play_button_keys(self):
        ''' Start new game on certain keypresses. '''
    
        if not self.stats.game_active:
            self._start_game()

    def _check_shoot_bullet(self):
        ''' Checks if the conditions are appropiate for shooting. '''

        if self.stats.game_active and \
           len(self.bullets) < self.settings.bullets_allowed:
            self._shoot_bullet()
        elif not self.stats.game_active and self._rocket_under_play_button():
            self._shoot_bullet()

    def _rocket_under_play_button(self):
        ''' Is the rocket under the play button? '''
    
        rocket = self.rocket.rect.centerx
        play_button = self.play_button.rect
        if play_button.left <= rocket <= play_button.right:
            return True

    def _shoot_bullet(self):
        ''' Create a new bullet and add it to the bullets group. '''
    
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        ''' Update position of bullets and get rid of old bullets. '''

        # Update bullets positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()
        self._check_play_button_collisions()

    def _check_play_button_collisions(self):
        ''' Checks for collisions between bullets and the play button. '''
    
        if pygame.sprite.spritecollideany(self.play_button, self.bullets) \
           and not self.stats.game_active:
            self._start_game()
    
    def _start_game(self):
        ''' Starts a new try. '''
    
        # Reset the game statistics.
        self.stats._reset_stats()
        self.settings.initialize_dynamic_settings()
        self.stats.game_active = True
        self.sb._prep_images()

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the rocket.
        self._create_fleet()
        self.rocket.center_rocket()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _create_fleet(self):
        ''' Create the fleet of aliens. '''
    
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        rocket_height = self.rocket.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height)
                                                         - rocket_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        ''' Create an alien and place it in the row. '''
    
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = 1.5 * alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        ''' Check if the fleet is at an edge, then update the positions of all
            aliens in the fleet. '''
    
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-rocket collisions.
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._rocket_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        ''' Respond appropriately if any aliens have reached an edge. '''
    
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        ''' Drop the entire fleet and change the fleet's direction. '''
    
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_bullet_alien_collisions(self):
        ''' Respond to bullet-alien collisions. '''
    
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        
        if collisions and self.stats.game_active:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self._start_new_level()

    def _start_new_level(self):
        ''' Starts a new level. '''

        # Destroy existing bullets and create new fleet
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        # Increase level.
        self.stats.level += 1
        self.sb.prep_level()

    def _rocket_hit(self):
        ''' Respond to the rocket being hit by an alien. '''

        if self.stats.rockets_left > 0:
            # Decrement rockets_left and update scoreboard.
            self.stats.rockets_left -= 1
            self.sb.prep_rockets()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the rocket.
            self._create_fleet()
            self.rocket.center_rocket()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        ''' Check if any aliens have reached the bottom of the screen. '''
    
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the rocket got hit.
                self._rocket_hit()
                break

    def _update_screen(self):
        ''' Update images on the screen, and flip to the new screen. '''

        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.rocket.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_play_button()

        pygame.display.flip()

    def _exit_game(self):
        ''' Last steps before quitting and quitting. '''
    
        with open(self.settings.hs_file, 'w') as f:
            json.dump(self.stats.high_score, f)
        sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()