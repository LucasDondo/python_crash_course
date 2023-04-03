import sys

import pygame


class Game:
    ''' An attempt to represent a game. '''

    def __init__(self):
        ''' Initialize main attributes. '''
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption('A game?')
        self.bg_color = (255, 212, 178)
        self.screen.fill(self.bg_color)
        self.character = Character(self)
        self.character.center_me()

    def start(self):
        ''' Main game loop. '''

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.flip()


class Character:
    ''' An attempt to represent a character. '''

    def __init__(self, game):
        ''' Initialize main attributes. '''
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('Bunny.bmp')
        # Resize image:
        self.image = pygame.transform.smoothscale(self.image, (500, 500))
        self.rect = self.image.get_rect()
        # self.image.fill(game.bg_color)

    def center_me(self):
        ''' Centers the character in the screen. '''
        self.rect.center = self.screen_rect.center
        self.screen.blit(self.image, self.rect)
