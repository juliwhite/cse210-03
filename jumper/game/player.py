
class Player:
    '''
    The player will guess a letter from a-z
    '''
    def __init__(self) -> None:
        self._player_input = None
    
    def get_input(self):
        return self._player_input
    
    def set_input(self, letter):
        self._player_input = letter
        print(self._player_input + " set")
