from ..player import Player

class AI(Player):
    ORDERED_CHARS = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

    def guess(self, state: str, eliminated_chars: set[str]) -> str:
        all_eliminated = {
            char.upper() 
            for char in set(state) | eliminated_chars
            if char != "_"
        }
        
        for candidate in self.ORDERED_CHARS:
            if candidate not in all_eliminated:
                return candidate
        
        assert False, "No more characters to guess"