import json

class Stats():
    ''' Track statistics for Alien Invasion. '''

    def __init__(self, ai):
        ''' Initialize statistics. '''

        self.ai = ai
        self.reset_stats()

        # Start Alien Invasion in an passive state.
        self.game_active = False

        # Get/Set high score.
        try:
            with open(self.ai.HS_FILE) as f:
                if json.load(f) >= 0:
                    self.hs = json.load(f)
                else:
                    self.hs = 0
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.hs = 0

    def reset_stats(self):
        ''' Initialize statistics that can change during the game. '''

        self.astronauts_left = self.ai.INITIAL_ASTRONAUTS
        self.score           = 0