from app.actions.add import add
from app.exceptions.validation import (
    MissingTitleException,
    MissingContentException,
    NoteAlreadyExistsException,
)
from app.models.note import Note

import pytest


def test_add_valid_note_no_due_date():
    # arrange
    notes = {}
    title = "title"
    content = "content"
    due_date = None
    expected = {
        title: Note(
            title=title,
            content=content,
            due_date=due_date,
        )
    }

    # act
    result = add(title, content, due_date, notes)

    # assert
    assert result == expected

def test_add_valid_note_with_due_date():
    # arrange
    notes = {}
    title = "title"
    content = "content"
    due_date = "2021-12-31"
    expected = {
        title: Note(
            title=title,
            content=content,
            due_date=due_date,
        )
    }

    # act
    result = add(title, content, due_date, notes)

    # assert
    assert result == expected

def test_add_missing_title():
    # arrange
    notes = {}
    title = ""
    content = "content"
    due_date = None

    # act & assert
    with pytest.raises(MissingTitleException):
        add(title, content, due_date, notes)

def test_add_missing_content():
    # arrange
    notes = {}
    title = "title"
    content = ""
    due_date = None

    # act & assert
    with pytest.raises(MissingContentException):
        add(title, content, due_date, notes)

def test_add_note_already_exists():
    # arrange
    notes = {
        "title": Note(
            title="title",
            content="content",
            due_date=None,
        )
    }
    title = "title"
    content = "content2"
    due_date = "arbitrary"

    # act & assert
    with pytest.raises(NoteAlreadyExistsException):
        add(title, content, due_date, notes)