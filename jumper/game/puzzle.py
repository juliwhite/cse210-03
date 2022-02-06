
import random

words = ["love", "family", "home", "smile"]

<<<<<<< HEAD
class Word:
    '''
    This class will direct the game. 
    '''
    def __init__(self) -> None:
        self._secret = random.choice(words)
        self._right_guesses = ['_' for letter in self._secret] #['_'] * len(self._secret)
        self._wrong_guesses = []

    def _get_word(self):
        display = ' '.join(self._right_guesses)
        return print(display)
    
    def _check_word(self, letter):
        letter = str(letter)
        if letter in self._secret:
            index = 0
            for i in self._secret:
                if i == letter:
                    self._right_guesses[index] = letter
                index += 1
        #print(self._right_guesses)
        else:
            if letter not in self._wrong_guesses:
                self._wrong_guesses.append(letter)
        #print(len(self._wrong_guesses))
    
    def _get_wrong_guesses(self):
        wrong_words = self._wrong_guesses
        #self._wrong_guesses = len(self._wrong_guesses)
        return len(wrong_words)
=======
class Puzzle:
    """ 
    This class will generate a secret work from a list. 
    """
    def __init__(self) -> None:
        self._word = random.choice(words) #choose a random word from list words

    def display_parachute(self):
        parachute = ['''
            ___''', '''
            /''',
        ]
    
>>>>>>> 6c25d91ce562d677feb1256e9321e739f93ba194
