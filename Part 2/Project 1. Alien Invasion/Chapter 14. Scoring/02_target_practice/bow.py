import pygame

class Bow:
    ''' An attempt to represent a bow. '''

    def __init__(self, tp):
        ''' Initialize main attributes. '''

        self.tp = tp
        self.screen = tp.screen
        self.screen_rect = tp.screen_rect
        self.settings = tp.settings
        self.speed = self.settings.bow_speed
        self.center_speed = self.settings.center_speed

        self.img = pygame.image.load('images/bow1.png')
        self.rect = self.img.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False
    
    def center(self):
        ''' Centers the bow. '''
    
        if self.rect.centery < self.screen_rect.centery:
            self.moving_down = True
            while self.rect.centery < self.screen_rect.centery:
                self.y += self.center_speed
                self.tp._update_screen()
            self.moving_down = False
        elif self.rect.centery > self.screen_rect.centery:
            self.moving_down = True
            while self.rect.centery > self.screen_rect.centery:
                self.y -= self.center_speed
                self.tp._update_screen()
            self.moving_down = False
        elif self.rect.centery == self.screen_rect.centery:
            pass

    def update(self):
        ''' Updates the bow position. '''
    
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

    def blit(self):
        ''' Starts main class actions. '''

        self.rect.y = self.y
        self.screen.blit(self.img, self.rect)