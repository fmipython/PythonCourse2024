from datetime import date
from app.models.note import Note
from app.ui.notes_list import list_all_notes


def test_list_all_notes_empty():
    """Test listing empty notes list."""
    notes = []
    expected = "Listing notes...\nNothing to list."
    assert list_all_notes(notes) == expected


def test_list_all_notes_single():
    """Test listing single note."""
    notes = [Note("Test note", "arbitrary content")]
    expected = "Listing notes...\n- Test note (Due: None)"
    assert list_all_notes(notes) == expected


def test_list_all_notes_multiple():
    """Test listing multiple notes."""
    titles = ["First note", "Second note", "Third note"]
    due_dates = [
        "2024-01-01",
        None,
        "2024-12-31",
    ]
    notes = [
        Note(title, "arbitrary content", due_date)
        for title, due_date in zip(titles, due_dates)

    ]
    expected = (
        "Listing notes...\n"
        f"- First note (Due: {due_dates[0]})\n"
        f"- Second note (Due: {due_dates[1]})\n"
        f"- Third note (Due: {due_dates[2]})"
    )
    assert list_all_notes(notes) == expected