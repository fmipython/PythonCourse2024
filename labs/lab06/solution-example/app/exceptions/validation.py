"""This module contains custom exceptions for validation errors"""


class ValidationException(Exception):
    """Just a base class for all validation exceptions
    so that one can easily catch 'em all pokemons"""
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class MissingTitleException(ValidationException):
    """Raised when the user has not provided a title for the note"""
    def __init__(self):
        super().__init__("Title is required.")

class MissingContentException(ValidationException):
    """Raised when the user has not provided content for the note"""
    def __init__(self):
        super().__init__("Content is required.")

class MissingContentOrDueDateException(ValidationException):
    """Raised when the user has not provided content or due date for the note,
    when trying to edit a note."""
    def __init__(self):
        super().__init__("No content or due date provided - no changes made to the note.")

class InvalidActionException(ValidationException):
    """Raised when the user has provided an invalid action"""
    def __init__(self):
        super().__init__("Invalid action.")

class NoteNotFoundException(ValidationException):
    """Raised when the note with the given title is not found"""
    def __init__(self, title):
        super().__init__(f"Note with title '{title}' not found.")

class NoteAlreadyExistsException(ValidationException):
    """Raised when the note with the given title already exists,
    e.g. when trying to add a note with a title that is already taken"""
    def __init__(self, title):
        super().__init__(f"Note with title '{title}' already exists.")
