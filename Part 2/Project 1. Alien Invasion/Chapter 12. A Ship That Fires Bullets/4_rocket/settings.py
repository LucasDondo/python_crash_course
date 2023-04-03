class Settings():
    ''' A class to store all settings for the Simple Rocket Game. '''

    def __init__(self):
        ''' Initialize the game's settings. '''

        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # Rocket settings.
        self.rocket_speed = 1.5
