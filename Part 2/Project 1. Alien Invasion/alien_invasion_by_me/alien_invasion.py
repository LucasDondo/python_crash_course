import sys
from time import sleep

import pygame

from stats       import Stats
from scoreboard  import Scoreboard
from play_button import PlayButton
from rocket      import Rocket
from bullet      import Bullet
from alien       import Alien
import sound_effects as se

class _AlienInvasion():
    ''' Overall class to to manage game assets and behavior. '''

    def __init__(self):
        ''' Initialize the game, and create game resources. '''

        pygame.init()
        pygame.display.set_caption('🚀 Alien Invasion! 👾')
        self.SCREEN             = pygame.display.set_mode(flags=pygame.FULLSCREEN)
        self.SCREEN_RECT        = self.SCREEN.get_rect()
        self.BG_COLOR           = (230, 230, 230)
        self.INITIAL_ASTRONAUTS = 3
        self.HS_FILE            = 'high_score.json'

        self.stats              = Stats(self)
        self.sb                 = Scoreboard(self)
        self.scorebar           = self.sb.scorebar
        self.play_button        = PlayButton(self)
        self.rocket             = Rocket(self)
        self.rocket.rect.bottom = self.scorebar.TOP

        self.bullets = pygame.sprite.Group()
        self.aliens  = pygame.sprite.Group()

    def run_game(self):
        ''' Start the main loop for the game. '''

        self._create_rows()
        self._initialize_speeds()

        while True:
            self._check_events()
            self.rocket.update()
            self._update_bullets()
            self.scorebar.update()

            if self.stats.game_active:
                self._update_aliens()

            self._show()

    def _initialize_speeds(self):
        ''' Initialize the speeds that change throughout the game. '''

        self.rocket_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed  = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # 💯 Scoring.
        self.alien_points = 100

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

        BULLETS_ALLOWED = 3

        if self.stats.game_active and \
           len(self.bullets) < BULLETS_ALLOWED:
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

        se.BULLET.play()
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

        se.BULLET.stop()
        se.PLAY.play()

        # 📈 Stats.
        self.stats.reset_stats()
        self.scorebar.reset()
        self.fleet_direction   = 1
        self.stats.game_active = True
        self.sb.prep_imgs()

        # 👾 Aliens.
        if self.play_button.transformed:
            self.aliens.empty()
            self._create_rows()

        # ❗ Bullets.
        self.bullets.empty()

        # 🚀 Rocket.
        pb_rect = self.play_button.rect
        if not pb_rect.left <= self.SCREEN_RECT.centerx <= pb_rect.right:
            self.rocket.center_rocket()

        # 🖱️ Mouse cursor.
        pygame.mouse.set_visible(False)

        # 🎮 Gameplay.
        self._initialize_speeds()

    def _create_rows(self):
        ''' Creates all the rows of aliens. '''

        alien        = Alien(self)
        alien_height = alien.rect.height
        spacing      = alien_height
        #
        available_space = self.scorebar.TOP - 2 * self.rocket.rect.height
        available_rows  = available_space // (alien_height + spacing)

        # Create rows
        for row_num in range(available_rows):
            y = spacing + row_num * (alien_height + spacing)
            self._create_row(y)

    def _create_row(self, y):
        ''' Creates a row of aliens. '''

        alien                 = Alien(self)
        alien_width           = alien.rect.width
        screen_width          = self.SCREEN_RECT.width
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

    def _check_fleet_edges(self):
        ''' Respond appropriately if any aliens have reached an edge. '''

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                # Look for aliens hitting the bottom of the screen.
                self._check_aliens_bottom()
                break

    def _change_fleet_direction(self):
        ''' Drop the entire fleet and change the fleet's direction. '''

        drop_speed = self._check_fleet_drop_speed()
        for alien in self.aliens.sprites():
            alien.rect.y += drop_speed
        self.fleet_direction *= -1

    def _check_fleet_drop_speed(self):
        ''' Blocks the fleet from crossing the sb line. '''

        drop_speed = 10
        # Check if the drop speed must change to avoid overpassing the limits.
        fleet_bottom = 0
        for alien in self.aliens.sprites():
            if alien.rect.bottom > fleet_bottom:
                fleet_bottom = alien.rect.bottom
        if self.scorebar.TOP - fleet_bottom < drop_speed:
            drop_speed = self.scorebar.TOP - fleet_bottom

        return drop_speed

    def _check_bullet_alien_collisions(self):
        ''' Respond to bullet-alien collisions. '''

        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True,
                                                                           True)
        if collisions:
            se.EXPLOSION.play()
            se.BULLET.stop()
            if self.stats.game_active:
                for aliens in collisions.values():
                    self.stats.score += self.alien_points * len(aliens)
                self.sb.check_hs()
                self.sb.prep_scores()
                if not self.aliens:
                    self.bullets.empty()
                    self._increase_speed()
                    self._create_rows()

    def _increase_speed(self):
        ''' Increase speed settings and alien point values. '''

        SPEEDUP_SCALE      = 1.05
        self.rocket_speed *= SPEEDUP_SCALE
        self.bullet_speed *= SPEEDUP_SCALE
        self.alien_speed  *= SPEEDUP_SCALE

        SCORE_SCALE       = 1.5
        self.alien_points = int(self.alien_points * SCORE_SCALE)

    def _rocket_hit(self):
        ''' Respond to the rocket being hit by an alien. '''

        se.ASTRONAUT_LOST.play()
        self.stats.astronauts_left -= 1
        self.sb._update_astronauts()
        self._show() # To see how things are positioned right when the disaster
                                                                     # happened.
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

    def _check_aliens_bottom(self):
        ''' Check if any aliens have reached the bottom of the screen. '''

        # Limit at scorebar, not before.
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.scorebar.TOP:
                # Treat this the same way as if the rocket got hit.
                self._rocket_hit()
                break

    def _show(self):
        ''' Update imgs on the screen, and flip to the new screen. '''

        # 📺 Screen.
        self.SCREEN.fill(self.BG_COLOR)
        # ❗ Bullets.
        for bullet in self.bullets.sprites():
            bullet.show()
        # 👾 Aliens.
        for alien in self.aliens.sprites():
            alien.show()
        # 💯 Scoreboard & Scorebar.
        self.sb.show()
        self.scorebar.show()
        # 🚀 Rocket.
        self.rocket.show()
        # ▶️ Play button.
        if not self.stats.game_active:
            self.play_button.show()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game.
    _ai = _AlienInvasion()
    _ai.run_game()