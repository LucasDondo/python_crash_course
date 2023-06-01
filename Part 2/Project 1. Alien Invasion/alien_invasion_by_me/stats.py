import json

class Stats():
    ''' Track statistics for Alien Invasion. '''

    def __init__(self, ai):
        ''' Initialize statistics. '''

        self.settings = ai.settings
        self.reset_stats()

        # Start Alien Invasion in an passive state.
        self.game_active = False

        # Get/Set high score.
        try:
            with open(self.settings.HS_FILE) as f:
                self.hs = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.hs = 0

    def reset_stats(self):
        ''' Initialize statistics that can change during the game. '''

        self.astronauts_left = self.settings.INITIAL_ASTRONAUTS
        self.score           = 0