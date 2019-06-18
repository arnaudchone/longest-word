# game.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
class Game:
    def __init__(self):
#        from nose.tools import set_trace
        import random
        import string
#       set_trace()
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)

    def __check_dictionary(self, word):
        import requests
        r = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = r.json()
        return response['found']
