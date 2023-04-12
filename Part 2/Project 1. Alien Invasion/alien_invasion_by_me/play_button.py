import pygame.font

class PlayButton:

    def __init__(self, ai):
        ''' Initialize play button attributes. '''

        self.screen = ai.screen
        self.screen_rect = self.screen.get_rect()

        self.img = pygame.image.load('images/play_button_50%.bmp')
        self.rect = self.img.get_rect()
        self.rect.center = self.screen_rect.center

    def transform(self):
        ''' Transforms the play button into play again button. '''
    
        self.img = pygame.image.load('images/play_again_button_50%.bmp')
        self.rect = self.img.get_rect()
        self.rect.center = self.screen_rect.center

    def blit(self):
        ''' Blit play button. '''
    
        self.screen.blit(self.img, self.rect)