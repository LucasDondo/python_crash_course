import pygame.font
from pygame.sprite import Group
import json

from astronaut import Astronaut

class Scoreboard:
    ''' A class to report scoring information. '''

    def __init__(self, ai):
        ''' Initialize scorekeeping attributes. '''

        self.ai = ai
        self.screen = ai.screen
        self.screen_rect = ai.screen_rect
        self.settings = ai.settings
        self.stats = ai.stats

        # ⚙️ Settings.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.Font('fonts/VarelaRound-Regular.ttf', 42)
        self.y_spacing = self.settings.sb_y_spacing
        self.x_spacing = self.settings.sb_x_spacing
        self.astronaut_centery = self.x_spacing

        self._prep_images()

    def _prep_images(self):
        ''' Prepare the initial score images. '''

        self._prep_astronauts()    
        self._prep_score()
        self._prep_hs()

    def _prep_astronauts(self):
        ''' Show how many astronauts are left. '''

        midscreen = self.screen_rect.width // 2

        self.astronauts = Group()
        for astronaut_num in range(self.stats.astronauts_left):
            astronaut = Astronaut()
            width = astronaut.rect.width
            astronaut.rect.top = self.y_spacing
            self.astronauts.add(astronaut)

            if self.stats.astronauts_left == 3:
                if astronaut_num == 0:
                    astronaut.rect.centerx = midscreen
                elif astronaut_num == 1:
                    astronaut.rect.right = midscreen - width // 2 - \
                                           self.x_spacing
                elif astronaut_num == 2:
                    astronaut.rect.left = midscreen + width // 2 + \
                                          self.x_spacing
            elif self.stats.astronauts_left == 2:
                if astronaut_num == 0:
                    astronaut.rect.left = midscreen + self.x_spacing // 2
                elif astronaut_num == 1:
                    astronaut.rect.right = midscreen - self.x_spacing // 2
            else:
                astronaut.rect.centerx = midscreen

    def _prep_score(self):
        ''' Turn the score into a rendered image. '''

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.x_spacing
        self.score_rect.centery = self.astronaut_centery
    
    def _prep_hs(self):
        ''' Turn the high score into a rendered image. '''

        hs = round(self.stats.hs, -1)
        hs_str = "{:,}".format(hs)
        self.hs_image = self.font.render(hs_str, True,
                                                self.text_color,
                                                self.settings.bg_color)
        
        # Center the high score at the top of the screen.
        self.hs_rect = self.hs_image.get_rect()
        self.hs_rect.right = self.screen_rect.right - self.x_spacing
        self.hs_rect.centery = self.astronaut_centery

    def _check_hs(self):
        ''' Check to see if there's a new high score. '''
    
        if self.stats.score > self.stats.hs:
            self.stats.hs = self.stats.score
            self._prep_hs()
            # Save it.
            with open('high_score.json', 'w') as f:
                json.dump(self.stats.hs, f)

    def show_score(self):
        ''' Draw scores and astronauts to the screen. '''

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hs_image, self.hs_rect)
        self.astronauts.draw(self.screen)