import pygame.font
from random import randint

class PlayButton:

    def __init__(self, ai):
        ''' Initialize play button attributes. '''

        self.screen      = ai.screen
        self.screen_rect = ai.screen_rect

        self.img         = pygame.image.load('images/play_button_50%.bmp')
        self.rect        = self.img.get_rect()
        self.rect.center = self.screen_rect.center

        self.transformed = False

    def transform(self):
        ''' Transforms the play button in multiple ways. '''
    
        # Play again button.
        self.img         = pygame.image.load('images/play_again_button_50%.bmp')
        self.rect        = self.img.get_rect()
        self.rect.center = self.screen_rect.center

        # Change x coordinates.
        lim_left          = self.rect.width // 2
        lim_right         = self.screen_rect.right - lim_left
        self.rect.centerx = randint(lim_left, lim_right)

        self.transformed = True

    def blit(self):
        ''' Blit play button. '''
    
        self.screen.blit(self.img, self.rect)