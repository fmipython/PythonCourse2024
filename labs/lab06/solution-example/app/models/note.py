"""Note model definition."""


from dataclasses import dataclass


@dataclass
class Note:
    """Shared core dataclass representing a note."""
    title: str
    content: str
    due_date: str | None = None  # за простота ползваме `str`,
    # иначе най-удачно е `datetime` обект или `int` timestamp
