# -*- coding: utf-8 -*-


class TracimError(Exception):
    pass


class RunTimeError(TracimError):
    pass


class ContentRevisionUpdateError(RuntimeError):
    pass


class ContentRevisionDeleteError(ContentRevisionUpdateError):
    pass


class ConfigurationError(TracimError):
    pass


class AlreadyExistError(TracimError):
    pass


class CommandError(TracimError):
    pass


class CommandAbortedError(CommandError):
    pass


class InvalidContentPathError(TracimError):
    """
    Exception raised when a content filename already exists.

    Attributes:
        filename -- content filename that already exists
    """

    def __init__(self, filename):
        self.filename = filename
