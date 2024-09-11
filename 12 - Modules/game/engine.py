from game.player import Player

from enum import Enum
import string


class GameState(Enum):
    ONGOING = 0
    WON = 1
    LOST = 2


class BesenitsaEngine:
    def __init__(self, word: str, player: Player):
        if len(word) < 3:
            raise ValueError("The word must have at least 3 characters!")

        if any(map(lambda c: c.upper() not in string.ascii_uppercase, word)):
            raise ValueError("The word must contain only ASCII letters!")

        self.player = player
        self.word = word.upper()
        self.revealed = {self.word[0], self.word[-1]} 
        self.__update_masked_word()

    def __update_masked_word(self):
        self.masked_word = "".join(
            char if char in self.revealed else "_"
            for char in self.word
        )

    def guess(self) -> GameState:
        attempt = self.player.guess(self.masked_word, self.revealed).upper()

        assert attempt not in self.revealed, "Attempted to guess a char again."

        self.revealed.add(attempt)
        self.__update_masked_word()

        if attempt not in self.word:
            self.player.take_fail()
            if self.player.is_dead:
                return GameState.LOST
        elif "_" not in self.masked_word:
            return GameState.WON
        
        return GameState.ONGOING


if __name__ == "__main__":
    # Executed when running `python3 -m game.engine`
    
    from game.players.mock_player import MockPlayer

    print("Testing win case...")
    player_win = MockPlayer(1, "oba")
    engine_win = BesenitsaEngine("foobar", player_win)

    assert engine_win.guess() == GameState.ONGOING
    assert engine_win.guess() == GameState.ONGOING
    assert engine_win.guess() == GameState.WON
    print("Test OK.")

    print("Testing lose case...")
    player_lose = MockPlayer(3, "asdg")
    engine_lose = BesenitsaEngine("foobar", player_lose)

    assert engine_lose.guess() == GameState.ONGOING
    assert engine_lose.guess() == GameState.ONGOING
    assert engine_lose.guess() == GameState.ONGOING
    assert engine_lose.guess() == GameState.LOST
    print("Test OK.")
