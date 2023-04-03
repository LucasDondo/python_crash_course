import sys
import pygame
from settings import Settings
from raindrop import Raindrop

class Rain():
    ''' An attempt to represent rain. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Just Rain')

        self.settings = Settings()

        self.rds = pygame.sprite.Group()
    
    def _create_row(self):
        ''' Creates a row of raindrops. '''
    
        rd = Raindrop(self)
        rd_width = rd.rect.width
        spacing = rd_width // 2
        available_space_side = self.screen_rect.width // 2 - rd_width // 2 - \
                               spacing
        available_rds_side = available_space_side // (spacing + rd_width)
        mid_screen = self.screen_rect.width // 2

        # Middle rd.
        rd.rect.centerx = self.screen_rect.centerx
        self.rds.add(rd)

        # Right rds.
        for rd in range(available_rds_side):
            count = rd
            rd = Raindrop(self)
            rd.rect.left = (mid_screen + rd_width // 2 + spacing) + count * (rd_width + spacing)
            self.rds.add(rd)

        # Left rds.
        for rd in range(available_rds_side):
            count = rd
            print(count)
            rd = Raindrop(self)
            rd.rect.right = (mid_screen - rd_width // 2 - spacing) - count * (rd_width + spacing)
            self.rds.add(rd)

        # Position on the top of the screen.
        for rd in self.rds:
            rd.rect.bottom = 0

    def _check_events(self):
        ''' Checks for and reacts to keyboard and mouse inputs. '''
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _renew_rds(self):
        ''' Deletes raindrops that got to the floor and creates new row. '''
    
        for rd in self.rds.sprites():
            if rd.fell():
                self.rds.remove(rd)
                self._create_row()

    def _update_screen(self):
        ''' Updates the main screen components. '''
    
        self.screen.fill((26, 82, 117))
        for rd in self.rds.sprites():
            rd.blitme()
        pygame.display.flip()

    def start(self):
        ''' Starts the main loop. '''
    
        self._create_row()
        while True:
            self._check_events()
            self._renew_rds()
            self.rds.update()
            self._update_screen()

if __name__ == '__main__':
    # Creates an instance and runs it.
    r = Rain()
    r.start()