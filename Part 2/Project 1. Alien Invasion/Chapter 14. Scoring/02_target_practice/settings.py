class Settings:
    ''' All game settings can be found here. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        # Target.
        self.target_width, self.target_height = 10, 100
        self.target_color = (0, 0, 0)
        self.target_speed = 1.0
        self.speedup_scale = 1.05

        # Screen.
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

        # General.
        self.animation_speed = 1.0
        self.arrow_animation_speed = 5.0