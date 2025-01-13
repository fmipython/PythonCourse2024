import pytest
from app.models.note import Note
from app.ui.note_details import note_details


def test_note_details_with_due_date():
    note = Note("Test Title", "Test Content", "2024-01-01")
    expected = """
    Title: Test Title
    ---
    Content: Test Content
    ---
    Due:2024-01-01
    """
    assert note_details(note) == expected

def test_note_details_without_due_date():
    note = Note("Test Title", "Test Content")
    expected = """
    Title: Test Title
    ---
    Content: Test Content
    ---
    No due date.
    """
    assert note_details(note) == expected

def test_note_details_with_empty_content():
    note = Note("Test Title", "")
    expected = """
    Title: Test Title
    ---
    Content: 
    ---
    No due date.
    """
    assert note_details(note) == expected