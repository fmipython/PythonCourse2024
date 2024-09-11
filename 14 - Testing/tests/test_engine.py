import unittest

from tests.mocks.mock_player import MockPlayer
from game.engine import BesenitsaEngine, GameState

class EngineTests(unittest.TestCase):
    def test_initialWord_isMaskedCorrectly(self):
        # Arrange
        player = MockPlayer(1, "a")
        sut = BesenitsaEngine("cat", player)
        expected = "C_T"

        # Act
        result = sut.masked_word

        # Assert
        self.assertEqual(result, expected)
    
    def test_cat_win(self):
        # Arrange
        player_win = MockPlayer(1, "a")
        sut = BesenitsaEngine("cat", player_win)

        # Act
        result = sut.guess()

        # Assert
        self.assertEqual(result, GameState.WON)

    def test_cat_lose(self):
        # Arrange
        player_win = MockPlayer(1, "b")
        sut = BesenitsaEngine("cat", player_win)

        # Act
        result = sut.guess()

        # Assert
        self.assertEqual(result, GameState.LOST)
    
    def test_foobar_win(self):
        player_win = MockPlayer(1, "oba")
        engine_win = BesenitsaEngine("foobar", player_win)

        self.assertEqual(engine_win.guess(), GameState.ONGOING)
        self.assertEqual(engine_win.guess(), GameState.ONGOING)
        self.assertEqual(engine_win.guess(), GameState.WON)

    def test_foobar_lose(self):
        player_lose = MockPlayer(3, "asdg")
        engine_lose = BesenitsaEngine("foobar", player_lose)

        self.assertEqual(engine_lose.guess(), GameState.ONGOING)
        self.assertEqual(engine_lose.guess(), GameState.ONGOING)
        self.assertEqual(engine_lose.guess(), GameState.ONGOING)
        self.assertEqual(engine_lose.guess(), GameState.LOST)

if __name__ == '__main__':
    unittest.main()