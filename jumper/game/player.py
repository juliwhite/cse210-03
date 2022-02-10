class Player:
    '''
    The player will guess a letter from a-z
    '''
    def __init__(self) -> None:
        """A person who play the game. 
        The responsibility of a Director is to control the sequence of play.
        """
        self._player_input = None
    
    def get_input(self):
        """Get the input from the terminal"""
        return self._player_input
    
    def set_input(self, letter):
        """Display the input from the player"""
        self._player_input = letter.lower()
        