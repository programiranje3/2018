"""Domain classes and functions related to the concept of author
"""


from datetime import date
from enum import Enum
import json

from classes2018.util import utility


class Lives(Enum):
    """The enum indicating the status of being alive or deceased.
    """


class Genre(Enum):
    """The enum indicating the music genres that the music package accepts.
    """


class Instrument(Enum):
    """The enum indicating the instruments that the music package accepts.
    """


class PoetryType(Enum):
    """The enum indicating the poetry types that the music package accepts.
    """


class Author:
    """The class describing the concept of author.
    It is assumed that an author is sufficiently described by his/her
    name, birth date, birth place, nationality, and whether he/she is still living or is deceased.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also defines the author's name and age as properties (the age property is calculated from birth date),
    as well as:
        - the definition static field
        - the class methods show_definition(cls) and get_instance(cls, name) (alternative constructor)
        - the static methods show_generic_definition(), format_author(author) and alive_or_deceased(alive)
    """


class AuthorEncoder(json.JSONEncoder):
    """JSON encoder for Author objects.
    Redefines the default(self, o) method of json.JSONEncoder.
    """


def json_to_py(author_json):
    """JSON decoder for Author objects (object_hook parameter in json.loads()).
    """


class Musician(Author):
    """The class describing the concept of musician.
    It is assumed that a musician is sufficiently described as an Author, with addition of his/her
    music genre and instrument(s). These are defined as properties of the Musician class.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclass.
    """


class Poet(Author):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as an Author, with addition of
    the type of poetry they create. This is defined as a property of the Poet class.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclass.
    """


class SingerSongwriter(Musician, Poet):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as a Musician who is simultaneously a Poet.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclasses.
    """


if __name__ == "__main__":

    pass
