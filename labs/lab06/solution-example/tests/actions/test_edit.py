import pytest
from app.actions.edit import edit
from app.models.note import Note

from app.exceptions.validation import (
    MissingContentOrDueDateException,
    MissingTitleException,
    NoteNotFoundException,
)


def test_edit_with_missing_title():
    with pytest.raises(MissingTitleException):
        edit("", "content", "due date", {})

def test_edit_with_missing_content_and_due_date():
    with pytest.raises(MissingContentOrDueDateException):
        edit("title", None, None, {"title": Note("title", "content", "due date")})

def test_edit_nonexistent_note():
    with pytest.raises(NoteNotFoundException):
        edit("title", "content", "due date", {})

def test_edit_content_only():
    notes = {"title": Note("title", "old content", "due date")}
    result = edit("title", "new content", None, notes)
    assert result["title"].content == "new content"
    assert result["title"].due_date == "due date"

def test_edit_due_date_only():
    notes = {"title": Note("title", "content", "old due date")}
    result = edit("title", None, "new due date", notes)
    assert result["title"].content == "content"
    assert result["title"].due_date == "new due date"

def test_edit_remove_due_date():
    notes = {"title": Note("title", "content", "due date")}
    result = edit("title", None, "none", notes)
    assert result["title"].due_date is None

def test_edit_both_fields():
    notes = {"title": Note("title", "old content", "old due date")}
    result = edit("title", "new content", "new due date", notes)
    assert result["title"].content == "new content"
    assert result["title"].due_date == "new due date"