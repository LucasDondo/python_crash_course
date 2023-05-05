import pygame
from pygame.sprite import Sprite

class Astronaut(Sprite):
    ''' An attempt to represent an astronaut. '''

    def __init__(self, ai):
        ''' Initialize main attributes. '''

        super().__init__()
        self.ai = ai

        self.image       = pygame.image.load('images/astronaut_30%.bmp')
        self.rect        = self.image.get_rect()
        self.rect.bottom = self.ai.screen_rect.bottom
    
    def transform(self):
        ''' OMG! No! The aliens attacked him! '''
    
        self.image  = pygame.image.load('images/astronaut_transformed_54px.bmp')
        self.rect = self.image.get_rect()
        self.rect.centery = self.ai.settings.astronaut_centery