from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, initial_hp: int):
        self.hp = initial_hp

    def take_fail(self):
        self.hp = max(0, self.hp - 1)

    @property
    def is_dead(self):
        return self.hp <= 0

    @abstractmethod
    def guess(self, state: str, eliminated_chars: set[str]) -> str:
        ...
    
