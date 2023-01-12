import sys
import pygame
from settings import Settings
from rocket import Rocket

class SimpleRocketGame():
    ''' An attempt to represent a Simple Rocket Game. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('The Simple Rocket Game')
        self.rocket = Rocket(self) # A Rocket instance is created within this
                                   # class.

        # Set the background color.
        self.bg_color = self.settings.bg_color

    def start(self):
        ''' Starts main class actions. '''
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()

    def _check_events(self):
        ''' Respond to keypresses and mouse events. '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        ''' Respond to keypresses. '''

        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = True

    def _check_keyup_events(self, event):
        ''' Respond to keyup events. '''

        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        if event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        if event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

    def _update_screen(self):
        ''' Update the images on the screen, and flip to the new screen. '''

        self.screen.fill(self.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Creates an instance and runs it.
    srg = SimpleRocketGame()
    srg.start()