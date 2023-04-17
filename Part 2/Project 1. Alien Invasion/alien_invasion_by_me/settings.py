from astronaut import Astronaut

class Settings:
    ''' A class to store all settings for Alien Invasion. '''

    def __init__(self):
        ''' Initialize the game's static settings. '''

        # 🖥️ Screen.
        self.bg_color = (230, 230, 230)

        # 👨🏼‍🚀 Astronauts.
        self.init_astronauts = 3

        # 💯 Scoreboard.
        self.sb_y_spacing = 10
        #
        astronaut = Astronaut()
        astronaut.rect.top = self.sb_y_spacing
        #
        self.sb_x_spacing = astronaut.rect.centery
        # Not settings but data needed...
        self.sb_bottom = astronaut.rect.height + 2 * self.sb_y_spacing
        # 👋🏼 I need the astronaut no longer.
        del astronaut

        # ❗ Bullet.
        self.bullets_allowed = 3

        # 👾 Alien.
        self.fleet_drop_speed = 10

        # 💨 How quickly the game speeds up.
        self.speedup_scale = 1.1

        # 📈 How quickly the alien point values increase.
        self.score_scale = 1.5

        self.hs_file = 'high_score.json'

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        ''' Initialize the settings that change throughout the game. '''
    
        self.rocket_speed = 1.5
        self.bullet_speed = 1.5
        self.alien_speed  = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # 💯 Scoring.
        self.alien_points = 50

    def increase_speed(self):
        ''' Increase speed settings and alien point values. '''
    
        self.rocket_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)