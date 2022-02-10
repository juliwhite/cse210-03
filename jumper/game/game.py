
from player import Player
from puzzle import Word
from parachute import Parachute

class Game:
    '''
    The game class will start the jumper game. 
    
    '''
    def __init__(self) -> None:
        '''
        Atributes: 
        _word > to pick random word from a list of words. 
        _play_game > It will be used in a while loop to keep playing the game
        _player > It will ask the user for a letter. 
        _parachute > it create a figure of the man with a parachute. 
        
        '''
        self._word = Word()
        self._play_game = True
        self._player = Player()
        self._parachute = Parachute()
    
    def start_jumper(self):
        '''
        Starts the game
        
        '''
        while self._play_game:
            self._do_output()
            self._get_input()
            self._do_update()
        

    def _do_output(self):
        '''
        Ask the user for a letter
        Display the figure of the man with a parachute.
        '''
        self._word._get_word()
        self._parachute._body(self._word._get_wrong_guesses())

    def _get_input(self):
        ask_player = input("\nGuess a letter [a-z]: ")
        self._player.set_input(ask_player)
    
    def _do_update(self):
        '''
        It will keep asking the user for an input letter and display answer. 
        '''
        self._word._check_word(self._player.get_input())
        self._parachute._body(self._word._get_wrong_guesses())
        if self._word._check_win() == 1 or self._word._get_wrong_guesses() == 7:
            self._play_game = False
