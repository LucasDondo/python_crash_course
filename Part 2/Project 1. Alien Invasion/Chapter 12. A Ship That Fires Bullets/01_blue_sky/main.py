import pygame
import sys


class BlueSky:
    ''' A simple representation of the blue sky. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.screen = pygame.display.set_mode((1200, 500))
        pygame.display.set_caption('Just Another Blue Sky.')
        self.screen.fill((0, 0, 255))
        pygame.display.flip()

    def start(self):
        ''' Loads the main program. '''

        while True:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


if __name__ == '__main__':
    blue_sky = BlueSky()
    blue_sky.start()
