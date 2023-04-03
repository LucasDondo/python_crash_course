class Stats:
    ''' All game stats can be found here. '''

    def __init__(self):
        ''' Initialize main attributes. '''

        self._reset()
        self.game_active = False
    
    def one_arrow_less(self):
        ''' The user lost one arrow. '''
    
        self.arrows_left -= 1
    
    def _reset(self):
        ''' Reset all stats. '''
    
        self.arrows_left = 3