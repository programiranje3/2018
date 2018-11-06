"""Utility functions of the package music
"""

from enum import Enum


def format_duration(seconds):
    """Converts a duration from seconds to string of the form '<mm>:<ss>'.
    """


def format_date(a_date):
    """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'.
    """


class Lives(Enum):
    """The enum indicating the status of being alive or deceased.
    """


def date_py_to_json(a_date):
    """Converts datetime.date objects to JSON.
    """


def date_json_to_py(iso_date):
    """Converts string formatted as 'YYYY-mm-dd' to datetime.date object.
    """


def get_project_dir():
    """Returns the Path object corresponding to the project root directory.
    """


def get_data_dir():
    """Returns the Path object corresponding to the data directory
    (by convention located right under the project root directory).
    """


if __name__ == '__main__':

    pass

