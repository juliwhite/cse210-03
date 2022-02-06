
from player import Player
from puzzle import Word
from parachute import Parachute

class Game:
    '''
    The game class will start the jumper game. 
    
    '''
    def __init__(self) -> None:
        self._word = Word()
        self._play_game = True
        self._player = Player()
        self._parachute = Parachute()
    
    def start_jumper(self):
        while self._play_game:
            self._do_output()
            self._get_input()
            self._do_update()
        

    def _do_output(self):
        self._word._get_word()
        self._parachute._body(self._word._get_wrong_guesses())

    def _get_input(self):
        ask_player = input("\nGuess a letter [a-z]: ")
        print(ask_player.lower())
        self._player.set_input(ask_player)
    
    def _do_update(self):
        self._word._check_word(self._player.get_input())
        self._parachute._body(self._word._get_wrong_guesses())

