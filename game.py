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
        return True
