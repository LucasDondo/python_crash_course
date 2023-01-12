import pygame

class Rocket():
    ''' An attempt to represent a rocket. '''
    # srg = Simple Rocket Game

    def __init__(self, srg):
        ''' Initialize main attributes. '''
        
        self.screen = srg.screen
        self.settings = srg.settings
        self.screen_rect = srg.screen.get_rect()

        # Load the rocket and its rect.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the ship's coordinates.
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        # Movement flags.
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False

    def update(self):
        ''' Update the rocket's position based on the movement flags. '''

        # Update the ship's coordinates value, not the rect.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
            # This confused me, but it is because the coordinates are used in
            # its absolute value.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # Update rect object from self.y and self.x.
        self.rect.y = self.y
        self.rect.x = self.x
        
    def blitme(self):
        ''' Draw the ship at its current location. '''

        self.screen.blit(self.image, self.rect)