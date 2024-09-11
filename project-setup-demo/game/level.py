from dataclasses import dataclass

@dataclass(frozen=True)
class Level:
    word: str
    failed_attempts: int