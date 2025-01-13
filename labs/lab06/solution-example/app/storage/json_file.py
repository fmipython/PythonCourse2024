"""JSON file storage module."""


import json
import os
from typing import Any

from app.models.note import Note


_CONTENT_KEY = "content"
_DUE_DATE_KEY = "due_date"

_ENCODING = "utf-8"

class JsonFileStorage:
    """Notes storage using a JSON file."""

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def load_all_notes(self) -> dict[str, Note]:
        """Return all persisted notes in the form of a dictionary
        with the note title as key and the `Note` object as value.
        """
        if not os.path.exists(self.__file_path):
            return {}

        with open(self.__file_path, "r", encoding=_ENCODING) as file:
            json_dict = json.load(file)

        results = self.__json_to_notes_dict(json_dict)
        return results

    def save_all_notes(self, notes_dict: dict[str, Note]):
        """Persist all notes to the file."""

        json_dict = self.__notes_dict_to_json(notes_dict)
        with open(self.__file_path, "w", encoding=_ENCODING) as file:
            json.dump(json_dict, file)


    def __json_to_notes_dict(self, json_data: dict[str, Any]) -> dict[str, Note]:
        return {
            title: Note(
                title=title,
                content=note_data[_CONTENT_KEY],
                due_date=note_data.get(_DUE_DATE_KEY),
            )
            for title, note_data in json_data.items()
        }

    def __notes_dict_to_json(self, notes_dict: dict[str, Note]) -> dict[str, Any]:
        return {
            title: {
                _CONTENT_KEY: note.content,
                _DUE_DATE_KEY: note.due_date,
            }
            for title, note in notes_dict.items()
        }
