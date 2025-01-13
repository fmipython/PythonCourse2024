"""Note details view CLI output."""


from app.models.note import Note


def note_details(note: Note) -> str:
    """Return a string representation of the note details."""

    return f"""
    Title: {note.title}
    ---
    Content: {note.content}
    ---
    {"Due:"+note.due_date if note.due_date else "No due date."}
    """