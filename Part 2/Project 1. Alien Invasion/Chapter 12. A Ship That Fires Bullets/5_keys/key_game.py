import sys
import pygame
from settings import Settings

class KeyGame():
    ''' An attempt to represent a Key Game. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('The Key Game')


    def start(self):
        ''' Starts main class actions. '''

        while True:
            self._check_events()

    def _check_events(self):
        ''' Checks and responds to events. '''

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event.key)
            elif event.type == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    # Creates an instance and runs it.
    tkg = KeyGame()
    tkg.start()