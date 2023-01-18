import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class SidewaysShooter():
    ''' Overall class to manage assets and behavior. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Sideways Shooter')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
    
    def _fire_bullet(self):
        ''' Creates a new bullet. '''
    
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    
    def _remove_old_bullets(self):
        ''' Get rid of old bullets. '''
    
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_rect.right:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        ''' Creates an alien fleet. '''
    
        alien = Alien(self)
        # Calculate available spaces.
        screen_width, screen_height = self.screen_rect.size
        alien_width, alien_height = alien.rect.size
        ship_width = self.ship.rect.width
        #
        available_space_x = screen_width - ship_width - 3 * alien_width
        available_space_y = screen_height - 2 * alien_height
        #
        available_columns = available_space_x // (2 * alien_width)
        available_rows = available_space_y // (2 * alien_height)

        # Create fleet.
        for column_number in range(available_columns):
            x = screen_width - 2 * alien_width - 2 * alien_width * column_number
            for row_number in range(available_rows):
                y = alien_height + 2 * alien_height * row_number
                self._create_alien(x, y)

    def _create_alien(self, x, y):
        ''' Creates an alien in the position (x, y). '''
    
        alien = Alien(self)
        alien.rect.x = x
        alien.rect.y = y
        self.aliens.add(alien)

    def _check_events(self):
        ''' Looks for and reacts to keyboard and mouse events. '''
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False

    def _update_screen(self):
        ''' Update the screen and main components. '''

        self.screen.fill(self.settings.bg_color)
        self.ship.update()
        self.bullets.update()
        self._remove_old_bullets()
        for alien in self.aliens.sprites():
                alien.blitme()
        pygame.display.flip()

    def start(self):
        ''' Runs the game. '''

        self._create_fleet()
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

if __name__ == '__main__':
    # Creates an instance and runs it.
    ss = SidewaysShooter()
    ss.start()