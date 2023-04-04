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

    def _create_rows(self):
        ''' Creates all the rows of stars. '''
    
        star = Star(self)
        star_height = star.rect.height
        screen_height = self.screen_rect.height
        midscreen = screen_height // 2
        spacing = star_height # For a better understanding of how this works.
        available_space_side = midscreen - star_height // 2 - spacing
        available_rows_side = available_space_side // (star_height + spacing)

        # Middle row.
        self._create_row(midscreen)

        # Down rows.
        for row_num in range(available_rows_side):
            y = midscreen + star_height + spacing + \
                row_num * (star_height + spacing)
            self._create_row(y)

        # Up rows.
        for row_num in range(available_rows_side):
            y = midscreen - star_height - spacing - \
                row_num * (star_height + spacing)
            self._create_row(y)

    def _create_row(self, y):
        ''' Creates a row of stars. '''
    
        star = Star(self)
        star_width = star.rect.width
        screen_width = self.screen_rect.width
        midscreen = screen_width // 2
        spacing = star_width # For a better understanding of how this works.
        available_space_side = midscreen - star_width // 2 - spacing
        available_stars_side = available_space_side // (star_width + spacing)

        # Middle star.
        star.rect.centerx = midscreen
        star.rect.centery = y
        self.stars.add(star)

        # Right stars.
        for star in range(available_stars_side):
            count = star
            star = Star(self)
            star.rect.left = (midscreen + star_width // 2 + spacing) + \
                             count * (star_width + spacing)
            star.rect.centery = y
            self.stars.add(star)

        # Left stars.
        for star in range(available_stars_side):
            count = star
            star = Star(self)
            star.rect.right = (midscreen - star_width // 2 - spacing) - \
                              count * (star_width + spacing)
            star.rect.centery = y
            self.stars.add(star)

    def start(self):
        ''' Starts main class actions. '''

        while True:
            self._check_events()
            self._create_rows()
            for star in self.stars.sprites():
                star.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    # Creates an instance and runs it.
    asfos = ASkyFullOfStars()
    asfos.start()