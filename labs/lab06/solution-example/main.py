"""Entry point script of the Note-Taking Application. Intended to be run from the command line."""

import argparse
import sys

from app.actions.add import add
from app.actions.delete import delete
from app.actions.edit import edit
from app.exceptions.validation import (
    ValidationException,
    InvalidActionException,
    MissingTitleException,
    MissingContentException,
)
from app.models.note import Note
from app.storage.json_file import JsonFileStorage
from app.ui.note_details import note_details
from app.ui.notes_list import list_all_notes
from app.ui.success_messages import (
    ADD_SUCCESS_MESSAGE,
    DELETE_SUCCESS_MESSAGE,
    EDIT_SUCCESS_MESSAGE,
)


JSON_FILE = "notes.json"  # Path to the JSON file where notes are stored


def _parse_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Command-line Note-Taking Application")
    parser.add_argument("action", choices=["add", "view", "delete", "edit", "list"],
                        help="What do you want to do?")
    parser.add_argument("--title", type=str,
                        help="Title of the note (required for all actions without `list`)")
    parser.add_argument("--content", type=str,
                         help="Content of the note (required for `add`, optional for `edit`)")
    parser.add_argument("--due-date", type=str,
                        help="Optional due date (for `add` and `edit` actions)")
    args = parser.parse_args()
    return args

def _require_title(args: argparse.Namespace) -> str:
    title = args.title
    if title is None:
        raise MissingTitleException
    return title

def _require_content(args: argparse.Namespace) -> str:
    content = args.content
    if content is None:
        raise MissingContentException
    return content


def action_output(
    args: argparse.Namespace,
    notes: dict[str, Note],
) -> tuple[str, dict[str, Note]]:
    """Return a tuple containing the output string and the updated notes dictionary."""

    match args.action:
        case "add":
            title = _require_title(args)
            content = _require_content(args)
            notes = add(title, content, args.due_date, notes)
            output = ADD_SUCCESS_MESSAGE.format(title=title)
        case "edit":
            title = _require_title(args)
            notes = edit(title, args.content, args.due_date, notes)
            output = EDIT_SUCCESS_MESSAGE
        case "delete":
            title = _require_title(args)
            notes = delete(title, notes)
            output = DELETE_SUCCESS_MESSAGE
        case "view":
            title = _require_title(args)
            note = notes[title]
            output = note_details(note)
        case "list":
            notes_list = list(notes.values())
            output = list_all_notes(notes_list)
        case _:
            raise InvalidActionException

    return output, notes


def main():
    """Main entry point of the application."""

    args = _parse_cli_args()
    storage = JsonFileStorage(JSON_FILE)

    notes = storage.load_all_notes()
    output, notes = action_output(args, notes)
    storage.save_all_notes(notes)

    print(output)


if __name__ == "__main__":
    try:
        main()
    except ValidationException as ve:
        print(ve, file=sys.stderr)  # хубаво е всички грешки да се пренасочват към STDERR
                                    # (`print` defaults to STDOUT)
        sys.exit(1)  # exit with a non-zero status code to indicate an error
