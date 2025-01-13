"""Add command implementation."""


from app.exceptions.validation import (
    MissingContentException,
    MissingTitleException,
    NoteAlreadyExistsException,
)
from app.models.note import Note


def add(
    title: str,
    content: str,
    due_date: str | None,
    notes: dict[str, Note]
) -> dict[str, Note]:
    """
    Attempt to create a new `Note` object with the given
    title, content, and due date (if provided).

    Return the updated notes dictionary.

    Raises an appropriate `ValidationException` subclass
    if the title is missing, the content is missing,
    or if the note with the given title already exists.
    """

    if not title:
        raise MissingTitleException

    if not content:
        raise MissingContentException

    if title in notes:
        raise NoteAlreadyExistsException(title)

    notes[title] = Note(
        title=title,
        content=content,
        due_date=due_date or None,
    )

    return notes
