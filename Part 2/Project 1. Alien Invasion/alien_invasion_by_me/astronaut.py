import pygame
from pygame.sprite import Sprite

class Astronaut(Sprite):
    ''' An attempt to represent an astronaut. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        super().__init__()

        self.img = pygame.image.load('images/astronaut_30%.bmp')
        self.rect = self.img.get_rect()
    
    def transform(self):
        ''' OMG! No! The aliens attacked him! '''
    
        self.img = pygame.image.load('images/astronaut_transformed_54px.bmp')
        self.rect = self.img.get_rect()