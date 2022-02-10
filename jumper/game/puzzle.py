from colorama import Fore
import random

words = ["love", "family", "home", "smile"]

class Word:
    '''
    This class will direct the game. 
    '''
    def __init__(self) -> None:
        """Contruct the word for the game.
        """
        self._secret = random.choice(words)
        self._right_guesses = ['_' for letter in self._secret] 
        self._wrong_guesses = []

    def _get_word(self):
        """Method to update the game progress with the guessed letters.
        """
        display = ' '.join(self._right_guesses)
        return print(display)
    
    def _check_word(self, letter):
        """Method to validate if the guess are right or wrong.
        """
        letter = str(letter)
        if letter in self._secret:
            index = 0
            for i in self._secret:
                if i == letter:
                    self._right_guesses[index] = letter
                index += 1
        else:
            if letter not in self._wrong_guesses:
                self._wrong_guesses.append(letter)
        
    
    def _get_wrong_guesses(self):
        """Method to validate if an user input is not just a letter.
        """
        wrong_words = self._wrong_guesses
        return len(wrong_words)

    def _check_win(self):
        """Method to validate if all the letter was correct.
        """
        if '_' not in self._right_guesses:
            print(f'{Fore.LIGHTGREEN_EX}Correct!')
            return 1