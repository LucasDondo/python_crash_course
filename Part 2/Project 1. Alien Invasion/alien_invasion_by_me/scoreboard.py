from   pygame.sprite import Group
import pygame.font
import json

from astronaut import Astronaut
from rocket    import ScoreBarRocket

class Scoreboard:
    ''' A class to report scoring information. '''

    def __init__(self, ai):
        ''' Initialize scorekeeping attributes. '''

        self.ai    = ai
        self.stats = ai.stats

        self.SCREEN             = self.ai.SCREEN
        self.SCREEN_RECT        = self.ai.SCREEN_RECT
        self.BG_COLOR           = self.ai.BG_COLOR
        self.INITIAL_ASTRONAUTS = self.ai.INITIAL_ASTRONAUTS

        self.prep_imgs()

        self.scorebar = ScoreBar(ai, self.SCOREBAR_BOTTOM)

    def prep_imgs(self):
        ''' Prepare the initial score imgs. '''

        self._create_astronauts()
        self.prep_scores()
        

    def _create_astronauts(self):
        ''' 👨🏻‍🚀 👨🏻‍🚀 👨🏻‍🚀 '''

        self.astronauts = Group()
        for astronaut in range(self.INITIAL_ASTRONAUTS):
            astronaut = Astronaut(self.ai)
            self.astronauts.add(astronaut)
        
        # Set astronaut-dependant constants.
        self.ASTRONAUT_CENTERY = self.astronauts.sprites()[0].CENTERY
        self.SCOREBAR_BOTTOM   = self.astronauts.sprites()[0].rect.top - 5
        self.X_SPACING         = self.SCREEN_RECT.bottom - \
                                                          self.ASTRONAUT_CENTERY

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
                astronauts[1].rect.right   = MIDSCREEN - WIDTH // 2 - \
                                                                  self.X_SPACING
            elif astronaut_n == 2:
                astronauts[2].rect.left    = MIDSCREEN + WIDTH // 2 + \
                                                                  self.X_SPACING

    def prep_scores(self):
        ''' Prepare score and high score to show. '''
    
        self.score_img, self.score_rect = self.prep_score(self.stats.score,
                                                                         'left')
        self.hs_img,    self.hs_rect    = self.prep_score(self.stats.hs,
                                                                        'right')

    def prep_score(self, score, pos):
        ''' Turn the score into a rendered img. '''

        TXT_COLOR = (30, 30, 30)
        FONT      = pygame.font.Font('fonts/VarelaRound-Regular.ttf', 42)

        rounded_score = round(score, -1)
        score_str     = "{:,}".format(rounded_score)
        score_img     = FONT.render(score_str, True, TXT_COLOR, self.BG_COLOR)

        score_rect         = score_img.get_rect()
        score_rect.centery = self.ASTRONAUT_CENTERY
        if pos == 'left':
            score_rect.left = self.X_SPACING
        elif pos == 'right':
            score_rect.right = self.SCREEN_RECT.right - self.X_SPACING
        else:
            raise ValueError("`pos` must be 'left' or 'right'.")
        
        return score_img, score_rect

    def check_hs(self):
        ''' Check to see if there's a new high score. '''

        if self.stats.score > self.stats.hs:
            self.stats.hs = self.stats.score
            self.prep_score(self.stats.hs, 'right')
            # Save it.
            with open(self.ai.HS_FILE, 'w') as f:
                json.dump(self.stats.hs, f)

    def show(self):
        ''' Draw scores and astronauts to the screen. '''

        self.SCREEN.blit(self.score_img, self.score_rect)
        self.SCREEN.blit(self.hs_img, self.hs_rect)
        self.astronauts.draw(self.SCREEN)

class ScoreBar:
    ''' An attempt to represent a scorebar. '''

    def __init__(self, ai, SCOREBAR_BOTTOM):
        ''' Initialize main attributes. '''

        self.ai          = ai
        self.SCREEN      = self.ai.SCREEN
        self.SCREEN_RECT = self.ai.SCREEN_RECT
        self.stats       = self.ai.stats
        self.SPEED       = 1
        self.RESET_SPEED = 5
        self.COLOR       = (0, 0, 0)

        self.rect   = pygame.Rect(0, 0, 0, 1)
        self.rocket = ScoreBarRocket(ai, SCOREBAR_BOTTOM)

        self.rect.centery = self.rocket.rect.centery
        self.TOP          = self.rocket.rect.top

        # Create the cleaning rect.
        self.cleaning_rect         = pygame.Rect(0, 0, 0,
                                                        self.rocket.rect.height)
        self.cleaning_rect.right   = self.SCREEN_RECT.right
        self.cleaning_rect.centery = self.rect.centery

    def reset(self):
        ''' Resets the bar w/ an animation using dirty blitting. '''

        self.cleaning_rect.width = 0
        self.cleaning_rect.right = self.SCREEN_RECT.right

        while self.rect.width > 0:
            self.rect.width          -= self.RESET_SPEED
            self.rocket.rect.right   -= self.RESET_SPEED
            self.cleaning_rect.width += self.RESET_SPEED
            self.cleaning_rect.left  -= self.RESET_SPEED

            pygame.draw.rect(self.SCREEN, self.ai.BG_COLOR, self.cleaning_rect)
            self.show()
            pygame.display.flip()

    def update(self):
        ''' Updates the sb's length. '''

        try:
            pct_score = self.stats.score * 100 / self.stats.hs
        except ZeroDivisionError:
            pct_score = 0
        pct_screen = pct_score * self.SCREEN_RECT.width / 100

        if self.rect.width < pct_screen:
            self.rect.width        += self.SPEED
            self.rocket.rect.right += self.SPEED

    def show(self):
        ''' Draws the sb to screen. '''

        pygame.draw.rect(self.SCREEN, self.COLOR, self.rect)
        self.rocket.show()