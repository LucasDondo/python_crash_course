import sys
import pygame
from random import randint
from star import Star

class BetterStars():
    ''' An attempt to represent a star game. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('A Sky Full of Better Stars')

        self.stars = pygame.sprite.Group()

    def _check_events(self):
        ''' Checks for keyboard and mouse inputs. '''
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_stars(self):
        ''' Creates the stars. '''
    
        # Define variables.
        star = Star(self)
        star_width, star_height = star.rect.size
        screen_lim_top = star_height
        screen_lim_right = self.screen_rect.width - star_width
        screen_lim_bottom = self.screen_rect.height - star_height
        screen_lim_left = star_width
        #
        available_space_x = self.screen_rect.width - (2 * star_width)
        available_columns = available_space_x // (2 * star_width)
        #
        available_space_y = self.screen_rect.height - (2 * star_height)
        available_rows = available_space_y // (2 * star_height)
        #
        available_stars = available_columns * available_rows

        # Set stars positions.
        q_stars = randint(1, available_stars)
        print(q_stars)
        for i in range(q_stars):
            star = Star(self)
            star.rect.centerx = randint(screen_lim_left, screen_lim_right)
            star.rect.centery = randint(screen_lim_top, screen_lim_bottom)
            self.stars.add(star)

    def start(self):
        ''' Starts main class actions. '''

        self._create_stars()
        while True:
            self._check_events()
            for star in self.stars.sprites():
                star.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    # Creates an instance and runs it.
    bs = BetterStars()
    bs.start()