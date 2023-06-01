import pygame
from random import randint

class PlayButton:

    def __init__(self, ai):
        ''' Initialize play button attributes. '''

        self.SCREEN      = ai.SCREEN
        self.SCREEN_RECT = ai.SCREEN_RECT

        self.image       = pygame.image.load('images/play_button_50%.bmp')
        self.rect        = self.image.get_rect()
        self.rect.center = self.SCREEN_RECT.center
        pygame.mouse.set_pos(self.rect.center)

        self.transformed = False

    def transform(self):
        ''' Transforms the play button in multiple ways. '''

        # Play again button.
        self.image       = pygame.image.load('images/play_again_button_50%.bmp')
        self.rect        = self.image.get_rect()
        self.rect.center = self.SCREEN_RECT.center

        # Change x coordinates.
        LIM_LEFT          = self.rect.width // 2
        LIM_RIGHT         = self.SCREEN_RECT.right - LIM_LEFT
        self.rect.centerx = randint(LIM_LEFT, LIM_RIGHT)

        if not self.transformed:
            self.transformed = True
        pygame.mouse.set_pos(self.rect.center)

    def show(self):
        ''' Blit play button. '''

        self.SCREEN.blit(self.image, self.rect)
        pygame.mouse.set_visible(True)