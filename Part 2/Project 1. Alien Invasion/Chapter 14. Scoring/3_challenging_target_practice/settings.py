class Settings:
    ''' All game settings can be found here. '''

    def __init__(self):
        ''' Initialize main static attributes. '''

        # Target settings.
        self.target_width, self.target_height = 10, 100
        self.target_color = (0, 0, 0)

        # Screen settings.
        self.bg_color = (255, 255, 255)

        # Bow.
        self.bow_speed = 1.0

        # Arrow.
        self.arrow_speed = 3.0

        # Play button.
        self.play_button_msg = "Let's go!"
        self.play_button_width, self.play_button_height = 200, 50
        self.play_button_text_color = (255, 255, 255)
        self.play_button_color = (0, 0, 0)

        # Speeding up the game.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        ''' Initialize main static attributes. '''
    
        self.target_speed = 1.0

    def speedup_game(self):
        ''' Increases the dynamic settings by speedup_scale. '''
    
        self.target_speed *= self.speedup_scale