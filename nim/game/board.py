import random

# TODO: Define the Board class here
class Board:
    def __init__(self):
        self._piles = []
        self.__prepare()
        

    def apply(self, move):
        
        if move._stones > self._piles[move._pile]:
            self._piles[move._pile] = 0
        else:
            self._piles[move._pile] = self._piles[move._pile] - move._stones

    def is_empty(self):
        for pile in self._piles:
            if pile > 0:
                return False
        
        return True

    def to_string(self):
        string = "- - - - - - - - - - - - - - - - - - - -"
        for i in range(len(self._piles)):
            string = string + f"\n{i} :  "
            for j in range(self._piles[i]):
                string = string + " O  "
        string = string + "\n- - - - - - - - - - - - - - - - - - - -"
        return string

    def __prepare(self):
        for i in range(0, random.randint(2,5)):
            self._piles.append(random.randint(1,9))
        