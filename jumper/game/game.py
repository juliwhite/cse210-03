from player import Player
from puzzle import Word
from parachute import Parachute

class Game:
    '''
    The game class will start the jumper game. 
    
    '''
    def __init__(self) -> None:
        """Contruct a new main.
        Args:
            self (main): an instance of main.
        """
        self._word = Word()
        self._play_game = True
        self._player = Player()
        self._parachute = Parachute()
    
    def start_jumper(self):
        """Starts the game by running the main game loop.
        Args:
            self(main): an instance of main.
        """
        while self._play_game:
            self._do_output()
            self._get_input()
            self._do_update()
        
    def _do_output(self):
        """Provides a hint for the player to complete the word.
        Args:
            self (main): An instance of main.
        """
        self._word._get_word()
        self._parachute._body(self._word._get_wrong_guesses())

    def _get_input(self):
        """Get the input from the player.
        Args:
            self(main): an instance of main.
        """
        ask_player = input("\nGuess a letter [a-z]: ")
        self._player.set_input(ask_player)
    
    def _do_update(self):
        """Update the answer if it is wrong or right.
        Args: 
            self(main): an instance of main.
        """
        self._word._check_word(self._player.get_input())
        self._parachute._body(self._word._get_wrong_guesses())
        if self._word._check_win() == 1:
            self._play_game = False