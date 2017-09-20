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
    Exception raised for errors in content path.

    Attributes:
        label_as_file -- content label that already exists
    """

    def __init__(self, label_as_file):
        self.label_as_file = label_as_file
