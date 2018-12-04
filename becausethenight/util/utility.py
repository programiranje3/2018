"""Utility functions of the package music
"""
import datetime
import time
from enum import Enum
from pathlib import Path

from becausethenight import settings


def format_duration(seconds):
    """Converts a duration from seconds to string of the form '<mm>:<ss>'.
    """

    return '%d:%02d' % (divmod(seconds, 60)) if seconds > 0 else 'unspecified'


def format_date(a_date):
    """Converts a date from datetime.date() to a string of the form '<month> <day>, <year>'.
    """

    # return a_date.strftime("%b %d, %Y") if a_date else 'unspecified'
    return datetime.datetime.strftime(a_date, "%b %d, %Y" ) if a_date else 'unspecified'


class Lives(Enum):
    """The enum indicating the status of being alive or deceased.
    """


def date_py_to_json(a_date):
    """Converts datetime.date objects to JSON.
    """

    return a_date.isoformat() if isinstance(a_date, datetime.date) else 'unknown'


def date_json_to_py(iso_date):
    """Converts string formatted as 'YYYY-mm-dd' to datetime.date object.
    """

    return datetime.date.fromisoformat(iso_date) if '-' in iso_date else None


def get_project_dir():
    """Returns the Path object corresponding to the project root directory.
    """

    return Path(settings.PROJECT_DIR)


def get_data_dir():
    """Returns the Path object corresponding to the data directory
    (by convention located right under the project root directory).
    """

    data_dir = Path(get_project_dir()) / 'data_dir'
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


if __name__ == '__main__':

    # get_data_dir()

    print(date_py_to_json(datetime.date(1978, 3, 2)))
    print(date_json_to_py(date_py_to_json(datetime.date(1978, 3, 2))))


