from ..player import Player
import string

class InputPlayer(Player):
    def guess(self, state: str, eliminated_chars: set[str]) -> str:
        result = "_"
        allowed = set(string.ascii_uppercase) - eliminated_chars - set(state) - {"_"}
        while result not in allowed:
            result = input("Guess a character: ").upper()
        return result