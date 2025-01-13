import pytest
from app.actions.delete import delete
from app.models.note import Note
from app.exceptions.validation import MissingTitleException, NoteNotFoundException


def test_delete_removes_note():
    notes = {"test": Note("test", "content")}
    result = delete("test", notes)
    assert "test" not in result

def test_delete_raises_missing_title():
    with pytest.raises(MissingTitleException):
        delete("", {})

def test_delete_raises_not_found():
    with pytest.raises(NoteNotFoundException):
        delete("nonexistent", {})

def test_delete_returns_dict():
    notes = {"test": Note("test", "content")}
    result = delete("test", notes)
    assert isinstance(result, dict)

def test_delete_preserves_other_notes():
    notes = {
        "test1": Note("test1", "content1"),
        "test2": Note("test2", "content2")
    }
    result = delete("test1", notes)
    assert "test2" in result
    assert result["test2"].content == "content2"