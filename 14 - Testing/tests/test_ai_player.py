import unittest

from game.players.ai import AI

BIG_HP = 42

class TestAIPlayer(unittest.TestCase):
    def test_firstGuess_isE(self):
        ai = AI(BIG_HP)

        guess = ai.guess("S_T", set())

        self.assertEqual(guess, "E")

if __name__ == '__main__':
    unittest.main()