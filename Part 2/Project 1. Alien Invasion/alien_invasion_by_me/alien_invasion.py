import sys
from time import sleep

import pygame

from settings import Settings
from stats import Stats
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

        self.screen      = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.bg_color    = self.settings.bg_color
        pygame.display.set_caption('🚀 Alien Invasion! 👾')

        self.stats       = Stats(self)
        self.sb          = Scoreboard(self)
        self.play_button = PlayButton(self)
        pygame.mouse.set_pos(self.play_button.rect.center)

        self.rocket  = Rocket(self)
        self.bullets = pygame.sprite.Group()
        self.aliens  = pygame.sprite.Group()

    def run_game(self):
        ''' Start the main loop for the game. '''

        self._create_rows()

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
                sys.exit()
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
            sys.exit()
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
    
        rocket      = self.rocket.rect.centerx
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
    
        # 📈 Stats.
        self.stats._reset_stats()
        self.settings.initialize_dynamic_settings()
        self.stats.game_active = True
        self.sb._prep_imgs()

        # 👾 Aliens.
        if self.play_button.transformed:
            self.aliens.empty()
            self._create_rows()
        
        # ❗ Bullets.
        self.bullets.empty()

        # 🚀 Rocket.
        self.rocket.center_rocket()

        # 🖱️ Mouse cursor.
        pygame.mouse.set_visible(False)

    def _create_rows(self):
        ''' Creates all the rows of aliens. '''
    
        alien         = Alien(self)
        alien_height  = alien.rect.height
        screen_height = self.screen_rect.height
        spacing       = alien_height
        #
        available_space = screen_height - self.settings.sb_height - \
                                                     2 * self.rocket.rect.height
        available_rows  = available_space // (alien_height + spacing)
        
        # Create rows
        for row_num in range(available_rows):
            y = spacing + row_num * (alien_height + spacing)
            self._create_row(y)

    def _create_row(self, y):
        ''' Creates a row of aliens. '''
    
        alien                 = Alien(self)
        alien_width           = alien.rect.width
        screen_width          = self.screen_rect.width
        midscreen             = screen_width // 2
        spacing               = alien_width
        available_space_side  = midscreen - alien_width // 2 - spacing
        available_aliens_side = available_space_side // (alien_width + spacing)

        # Middle alien, reusing the alien before created.
        alien.rect.centerx = midscreen
        alien.rect.centery = y
        self.aliens.add(alien)

        # Right aliens.
        for alien in range(available_aliens_side):
            count              = alien
            alien              = Alien(self)
            alien.rect.left    = (midscreen + alien_width // 2 + spacing) + \
                                                 count * (alien_width + spacing)
            alien.rect.centery = y
            self.aliens.add(alien)

        # Left aliens.
        for alien in range(available_aliens_side):
            count              = alien
            alien              = Alien(self)
            alien.rect.right   = (midscreen - alien_width // 2 - spacing) - \
                                                 count * (alien_width + spacing)
            alien.rect.centery = y
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
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True
                                                                         , True)
        if collisions and self.stats.game_active:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb._prep_score()
            self.sb._check_hs()
            if not self.aliens:
                self.bullets.empty()
                self._create_rows()
                self.settings.increase_speed()

    def _rocket_hit(self):
        ''' Respond to the rocket being hit by an alien. '''

        self.stats.astronauts_left -= 1
        self.sb._update_astronauts()
        if self.stats.astronauts_left > 0:
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the rocket.
            self._create_rows()
            self.rocket.center_rocket()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.play_button.transform()
            pygame.mouse.set_pos(self.play_button.rect.center)
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        ''' Check if any aliens have reached the bottom of the screen. '''
    
        bottom_lim = self.screen_rect.height - self.settings.sb_height + \
                     self.settings.sb_y_spacing # Limit at astronaut's top, not 
                                                # before.
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= bottom_lim:
                # Treat this the same as if the rocket got hit.
                self._rocket_hit()
                break

    def _update_screen(self):
        ''' Update imgs on the screen, and flip to the new screen. '''

        self.screen.fill(self.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.rocket.blitme()

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.blit()

        pygame.display.flip()        

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()