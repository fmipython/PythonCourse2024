"""All notes list CLI output."""


from app.models.note import Note


def list_all_notes(notes: list[Note]) -> str:
    """Return a string representation of all notes in the list."""

    header = "Listing notes..."

    if len(notes) == 0:
        return f"{header}\nNothing to list."

    return header + "\n" + "\n".join(
        f"- {note.title} (Due: {note.due_date})"
        for note in notes
    )
