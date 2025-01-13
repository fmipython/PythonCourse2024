"""Delete command implementation."""


from app.models.note import Note

from app.exceptions.validation import (
    MissingTitleException,
    NoteNotFoundException,
)


def delete(title: str, notes: dict[str, Note]) -> dict[str, Note]:
    """
    Attempt to delete the note with the given title.
    
    Return the updated notes dictionary.
    
    Raises an appropriate `ValidationException` subclass
    if the title is missing or if the note with the given
    title does not exist.
    """

    if not title:
        raise MissingTitleException

    if title not in notes:
        raise NoteNotFoundException(title)

    del notes[title]

    return notes
