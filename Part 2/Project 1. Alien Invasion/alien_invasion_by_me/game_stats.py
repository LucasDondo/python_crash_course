import json

class GameStats():
    ''' Track statistics for Alien Invasion. '''

    def __init__(self, ai):
        ''' Initialize statistics. '''

        self.settings = ai.settings
        self._reset_stats()

        # Start Alien Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        try:
            with open(self.settings.hs_file) as f:
                self.hs = json.load(f)
        except FileNotFoundError:
            self.hs = 0

    def _reset_stats(self):
        ''' Initialize statistics that can change during the game. '''

        self.astronauts_left = self.settings.init_astronauts
        self.score = 0