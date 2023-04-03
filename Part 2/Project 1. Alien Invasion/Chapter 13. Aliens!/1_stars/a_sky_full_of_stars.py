import sys
import pygame
from star import Star

class ASkyFullOfStars():
    ''' An attempt to represent a star game. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('A Sky Full of Stars')

        self.stars = pygame.sprite.Group()

    def _check_events(self):
        ''' Checks for keyboard and mouse inputs. '''
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _create_row(self):
        ''' Creates a row of stars. '''
    
        # Define variables.
        star = Star(self)
        star_width, star_height = star.rect.size
        #
        available_space_x = self.screen_rect.width - (2 * star_width)
        available_columns = available_space_x // (2 * star_width)
        #
        available_space_y = self.screen_rect.height - (2 * star_height)
        available_rows = available_space_y // (2 * star_height)

        # Create "matrix".
        for row_number in range(available_rows):
            for column_number in range(available_columns):
                star = Star(self)
                star.rect.x = star_width + (2 * star_width * column_number)
                star.rect.y = star_height + (2 * star_height * row_number)
                self.stars.add(star)

    def start(self):
        ''' Starts main class actions. '''

        while True:
            self._check_events()
            self._create_row()
            for star in self.stars.sprites():
                star.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    # Creates an instance and runs it.
    asfos = ASkyFullOfStars()
    asfos.start()