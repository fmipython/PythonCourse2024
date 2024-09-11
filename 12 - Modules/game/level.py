from dataclasses import dataclass

@dataclass(frozen=True)
class Level:
    word: str
    failed_attempts: int


EASY = Level(word="SCRIPT", failed_attempts=10)
MEDIUM = Level(word="PYTHONIC", failed_attempts=8)
HARD = Level(word="INTERPRETER", failed_attempts=3)
PESHO_BAFTATA = Level(word="ILLUMINATI", failed_attempts=1)