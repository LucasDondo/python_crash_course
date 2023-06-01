from   pygame.sprite import Group
import pygame.font
import json

from astronaut import Astronaut

class Scoreboard:
    ''' A class to report scoring information. '''

    def __init__(self, ai):
        ''' Initialize scorekeeping attributes. '''

        self.ai       = ai
        self.settings = ai.settings
        self.stats    = ai.stats

        self.SCREEN             = self.ai.SCREEN
        self.SCREEN_RECT        = self.ai.SCREEN_RECT
        self.BG_COLOR           = self.ai.BG_COLOR
        self.INITIAL_ASTRONAUTS = self.settings.INITIAL_ASTRONAUTS

        # ⚙️ Settings.
        self.TXT_COLOR         = (30, 30, 30)
        self.FONT              = pygame.font.Font(
                                            'fonts/VarelaRound-Regular.ttf', 42)
        self.X_SPACING         = self.settings.SB_X_SPACING
        self.ASTRONAUT_CENTERY = self.settings.ASTRONAUT_CENTERY

        self.prep_imgs()

    def prep_imgs(self):
        ''' Prepare the initial score imgs. '''

        self._create_astronauts()    
        self._prep_score()
        self._prep_hs()

    def _create_astronauts(self):
        ''' 👨🏻‍🚀 👨🏻‍🚀 👨🏻‍🚀 '''

        self.astronauts = Group()
        for astronaut in range(self.INITIAL_ASTRONAUTS):
            astronaut = Astronaut(self.ai)
            self.astronauts.add(astronaut)
        
        self._update_astronauts()

    def _update_astronauts(self):
        ''' How many of them have been transformed!? '''

        astronauts = self.astronauts.sprites()

        # 👨🏻‍🚀 ➡️ 👽    
        if self.stats.astronauts_left   == 2:
            astronauts[2].transform()
        elif self.stats.astronauts_left == 1:
            astronauts[1].transform()
        elif self.stats.astronauts_left == 0:
            astronauts[0].transform()

        # Position on screen.
        for astronaut_n in range(self.INITIAL_ASTRONAUTS):
            WIDTH     = astronauts[0].rect.width
            MIDSCREEN = self.SCREEN_RECT.width // 2

            if astronaut_n == 0:
                astronauts[0].rect.centerx = MIDSCREEN
            elif astronaut_n == 1:
                astronauts[1].rect.right = MIDSCREEN - WIDTH // 2 - \
                                                                  self.X_SPACING
            elif astronaut_n == 2:
                astronauts[2].rect.left = MIDSCREEN + WIDTH // 2 + \
                                                                  self.X_SPACING

    def _prep_score(self):
        ''' Turn the score into a rendered img. '''

        rounded_score  = round(self.stats.score, -1)
        score_str      = "{:,}".format(rounded_score)
        self.score_img = self.FONT.render(score_str, True, self.TXT_COLOR,
                                                                  self.BG_COLOR)

        # Display the score at the top right of the screen.
        self.score_rect         = self.score_img.get_rect()
        self.score_rect.left    = self.X_SPACING
        self.score_rect.centery = self.ASTRONAUT_CENTERY

    def _prep_hs(self):
        ''' Turn the high score into a rendered img. '''

        hs          = round(self.stats.hs, -1)
        hs_str      = "{:,}".format(hs)
        self.hs_img = self.FONT.render(hs_str, True, self.TXT_COLOR,
                                                                  self.BG_COLOR)

        # Center the high score at the top of the screen.
        self.hs_rect         = self.hs_img.get_rect()
        self.hs_rect.right   = self.SCREEN_RECT.right - self.X_SPACING
        self.hs_rect.centery = self.ASTRONAUT_CENTERY

    def _check_hs(self):
        ''' Check to see if there's a new high score. '''

        if self.stats.score > self.stats.hs:
            self.stats.hs = self.stats.score
            self._prep_hs()
            # Save it.
            with open(self.settings.HS_FILE, 'w') as f:
                json.dump(self.stats.hs, f)

    def show(self):
        ''' Draw scores and astronauts to the screen. '''

        self.SCREEN.blit(self.score_img, self.score_rect)
        self.SCREEN.blit(self.hs_img, self.hs_rect)
        self.astronauts.draw(self.SCREEN)