import pygame.font
from random import randint

class PlayButton:

    def __init__(self, ai):
        ''' Initialize play button attributes. '''

        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()

        self.img = pygame.image.load('images/play_button_50%.bmp')
        self.rect = self.img.get_rect()
        self.rect.center = self.screen_rect.center

    def transform(self):
        ''' Transforms the play button in multiple ways. '''
    
        # Play again button.
        self.img = pygame.image.load('images/play_again_button_50%.bmp')
        self.rect = self.img.get_rect()
        self.rect.center = self.screen_rect.center

        # Change x coordinates.
        limit_left = self.rect.width // 2
        limit_right = self.screen_rect.right - limit_left
        self.rect.centerx = randint(limit_left, limit_right)

    def blit(self):
        ''' Blit play button. '''
    
        self.screen.blit(self.img, self.rect)