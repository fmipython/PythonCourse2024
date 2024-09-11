from game.player import Player

class MockPlayer(Player):
    def __init__(self, initial_hp: int, guesses: str):
        self.guesses = guesses
        self.__index = 0
        super().__init__(initial_hp)

    def guess(self, state: str, eliminated_chars: set[str]) -> str:
        result = self.guesses[self.__index]
        self.__index += 1
        return result