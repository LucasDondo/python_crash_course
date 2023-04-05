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
    
    def _create_row(self):
        ''' Creates a row of raindrops. '''
    
        raindrop = Raindrop(self)
        # Defines area and limits.
        available_space_x = self.screen_rect.width
        raindrop_width = raindrop.rect.width
        q_raindrops = available_space_x // (2 * raindrop_width)

        # Creates row (group) w/ q_raindrops raindrops.
        self.raindrops = pygame.sprite.Group()
        for raindrop in range(q_raindrops):
            x = 2 * raindrop_width * raindrop
            raindrop = Raindrop(self)
            raindrop.rect.x = x
            self.raindrops.add(raindrop)

    def _check_events(self):
        ''' Checks for and reacts to keyboard and mouse inputs. '''
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    def _clean_raindrops(self):
        ''' Deletes raindrops that got to the floor. '''
    
        for raindrop in self.raindrops.sprites():
            if raindrop.fell():
                self.raindrops.remove(raindrop)

    def _update_screen(self):
        ''' Updates the main screen components. '''
    
        self.screen.fill((26, 82, 117))
        for raindrop in self.raindrops.sprites():
            raindrop.blitme()
        pygame.display.flip()

    def start(self):
        ''' Starts the main loop. '''
    
        self._create_row()
        while True:
            self._check_events()
            self.raindrops.update()
            self._clean_raindrops()
            self._update_screen()
            print(len(self.raindrops))

if __name__ == '__main__':
    # Creates an instance and runs it.
    r = Rain()
    r.start()