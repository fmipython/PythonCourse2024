"""Edit command implementation."""


from app.exceptions.validation import (
    MissingContentOrDueDateException,
    MissingTitleException,
    NoteNotFoundException,
)
from app.models.note import Note


def edit(
    title: str,
    content: str | None,
    due_date: str | None,
    notes: dict[str, Note]
) -> dict[str, Note]:
    """
    Attempt to create a new `Note` object with the given
    title, content, and due date (if provided).

    If `due_date` is `"none"` then the due date is reset to None.

    If `due_date` or `content` is not provided,
    the existing note's value of the corresp. field is preserved.

    Return the updated notes dictionary.

    Raises an appropriate `ValidationException` subclass
    if the title is missing, both content and die date are missing,
    or if the note with the given title does not exist.
    """

    if not title:
        raise MissingTitleException

    if not content and not due_date:
        raise MissingContentOrDueDateException

    if title not in notes:
        raise NoteNotFoundException(title)

    existing_note = notes[title]

    if due_date is None:
        new_due_date = existing_note.due_date
    elif due_date.strip().lower() == "none":
        new_due_date = None
    else:
        new_due_date = due_date

    notes[title] = Note(
        title=title,
        content=content or existing_note.content,
        due_date=new_due_date,
    )

    return notes
