class GameStats():
    ''' Track statistics for Alien Invasion. '''

    def __init__(self, ai_game):
        ''' Initialize statistics. '''

        self.settings = ai_game.settings
        self._reset_stats()

    def _reset_stats(self):
        ''' Initialize statistics that can change during the game. '''

        self.ships_left = self.settings.ship_limit