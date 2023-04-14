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

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self._prep_images()        

    def _prep_images(self):
        ''' Prepare the initial score images. '''
    
        self.prep_score()
        self.prep_high_score()
        self.prep_astronauts()

    def prep_score(self):
        ''' Turn the score into a rendered image. '''

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        ''' Turn the high score into a rendered image. '''

        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                self.text_color,
                                                self.settings.bg_color)
        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 20
        self.high_score_rect.top = 20

    def check_high_score(self):
        ''' Check to see if there's a new high score. '''
    
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
            # Save it.
            with open('high_score.json', 'w') as f:
                json.dump(self.stats.high_score, f)

    def prep_astronauts(self):
        ''' Show how many astronauts are left. '''

        midscreen = self.screen_rect.width // 2

        self.astronauts = Group()
        for astronaut_num in range(self.stats.astronauts_left):
            astronaut = Astronaut()
            width = astronaut.rect.width
            astronaut.rect.y = 20
            self.astronauts.add(astronaut)

            if self.stats.astronauts_left == 3:
                if astronaut_num == 0:
                    astronaut.rect.centerx = midscreen
                elif astronaut_num == 1:
                    astronaut.rect.right = midscreen - width // 2 - 20
                elif astronaut_num == 2:
                    astronaut.rect.left = midscreen + width // 2 + 20
            elif self.stats.astronauts_left == 2:
                if astronaut_num == 0:
                    astronaut.rect.left = midscreen + 10
                elif astronaut_num == 1:
                    astronaut.rect.right = midscreen - 10
            else:
                astronaut.rect.centerx = midscreen

    def show_score(self):
        ''' Draw scores and astronauts to the screen. '''

        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.astronauts.draw(self.screen)