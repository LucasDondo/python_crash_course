class Settings():
    ''' Loads all game settings. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        # Screen settings.
        self.screen_height = 500
        self.screen_width = 1200
        self.bg_color = (0, 0, 0)

        # Ship settings.
        self.ship_speed = .5

        # Bullet settings.
        self.bullet_speed = 1.0
        self.bullet_height = 5
        self.bullet_width = 15
        self.bullet_color = (221, 83, 83)