from astronaut import Astronaut

class Settings:
    ''' A class to store all settings for Alien Invasion. '''

    def __init__(self, ai):
        ''' Initialize the game's static settings. '''

        # 📺 Screen.
        self.BG_COLOR = (230, 230, 230)

        # 👨🏼‍🚀 Astronauts.
        self.INITIAL_ASTRONAUTS = 3

        # 💯 Scoreboard.
        self.SB_Y_SPACING = 5
        #
        astronaut              = Astronaut(ai)
        self.ASTRONAUT_TOP     = astronaut.rect.top
        self.ASTRONAUT_CENTERY = astronaut.rect.centery
        del astronaut
        #
        self.SB_X_SPACING = ai.SCREEN_RECT.bottom - self.ASTRONAUT_CENTERY
        # Scorebar.
        self.SB_ANIMATION_SPEED       = 1
        self.SB_RESET_ANIMATION_SPEED = 5
        self.SB_COLOR                 = (0, 0, 0)

        # ❗ Bullet.
        self.BULLETS_ALLOWED = 3

        # 👾 Alien.
        self.FLEET_DROP_SPEED = 10

        # 💨 How quickly the game speeds up.
        self.SPEEDUP_SCALE = 1.05

        # 📈 How quickly the alien point values increase.
        self.SCORE_SCALE = 1.5

        self.HS_FILE = 'high_score.json'

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        ''' Initialize the settings that change throughout the game. '''
    
        self.rocket_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed  = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # 💯 Scoring.
        self.alien_points = 100

    def increase_speed(self):
        ''' Increase speed settings and alien point values. '''
    
        self.rocket_speed *= self.SPEEDUP_SCALE
        self.bullet_speed *= self.SPEEDUP_SCALE
        self.alien_speed  *= self.SPEEDUP_SCALE

        self.alien_points = int(self.alien_points * self.SCORE_SCALE)