import json

class GameStats():
    ''' Track statistics for Alien Invasion. '''

    def __init__(self, ai_game):
        ''' Initialize statistics. '''

        self.settings = ai_game.settings
        self._reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        try:
            with open(self.settings.hs_file) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0

    def _reset_stats(self):
        ''' Initialize statistics that can change during the game. '''

        self.rockets_left = self.settings.rocket_limit
        self.score = 0
        self.level = 1