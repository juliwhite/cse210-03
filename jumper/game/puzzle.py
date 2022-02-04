
import random

words = ["love", "family", "home", "smile"]

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
    