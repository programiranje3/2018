"""Domain classes and functions related to the concept of author
"""


from datetime import date
from enum import Enum
import json

import jsonpickle

from becausethenight.util import utility


class Lives(Enum):
    """The enum indicating the status of being alive or deceased.
    """

    ALIVE = 1,
    DECEASED = 0,


class Genre(Enum):
    """The enum indicating the music genres that the music package accepts.
    """

    ROCK = 1,
    BLUES = 2,
    SOUL = 3,
    OTHER = 4


class Instrument(Enum):
    """The enum indicating the instruments that the music package accepts.
    """

    GUITAR = 1,
    BASS = 2,
    DRUMS = 3,
    KEYBOARDS = 4,
    OTHER = 5


class PoetryType(Enum):
    """The enum indicating the poetry types that the music package accepts.
    """

    LYRIC = 1,
    DRAMATIC = 2,
    EPIC = 3,
    OTHER = 4


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

    definition = 'Creator of artwork'

    def __init__(self, name, birth_date=None, birth_place='unknown', nationality='unknown', alive=Lives.ALIVE):
        self.name = name
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.nationality = nationality
        self.alive = alive

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return date.today().year - self.birth_date.year if self.birth_date and isinstance(self.birth_date, date) else 0

    def __str__(self):
        author = self.name
        author += ': ' + str(self.birth_date) + ', ' if self.birth_date and isinstance(self.birth_date, date) else ''
        author += self.birth_place + ', ' if self.birth_place and isinstance(self.birth_place, str) else ''
        author += self.nationality + ', ' if self.nationality and isinstance(self.nationality, str) else ''
        author += 'alive, ' if self.alive == Lives.ALIVE else 'deceased' if self.alive == Lives.DECEASED else 'unknown if alive or deceased'
        return author

    def __eq__(self, other):
        return isinstance(other, Author) and self.name == other.name

    @classmethod
    def show_definition(cls):
        print(cls.definition)

    @classmethod
    def get_instance(cls, name):
        return cls(name)

    @staticmethod
    def format_author(author):
        return author.name if author and isinstance(author, Author) else 'unknown'

    @staticmethod
    def alive_or_deceased(author):
        a = ''
        if author:
            if isinstance(author, Author):
                a += 'alive' if author.alive == Lives.ALIVE else 'deceased' if author.alive == Lives.DECEASED else 'unknown if alive or deceased'
            else:
                a += author if isinstance(author, str) else ''
        else:
            a += 'unknown'

        return a


class AuthorEncoder(json.JSONEncoder):
    """JSON encoder for Author objects.
    Redefines the default(self, o) method of json.JSONEncoder.
    """

    def default(self, o):
        if isinstance(o, Author):
            d = o.__dict__.copy()
            d['birth_date'] = utility.date_py_to_json(o.birth_date)
            d['alive'] = 'true' if o.alive == Lives.ALIVE \
                else 'false' if o.alive == Lives.DECEASED \
                else 'unknown'
            return {'__Author__': d}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


def json_to_py(author_json):
    """JSON decoder for Author objects (object_hook parameter in json.loads()).
    """

    if '__Author__' in author_json:
        a = Author('unknown')
        a.__dict__.update(author_json['__Author__'])
        a.birth_date = utility.date_json_to_py(a.__dict__['birth_date'])
        a.alive = Lives.ALIVE if a.__dict__['alive'] == 'true' \
            else Lives.DECEASED if a.__dict__['alive'] == 'false' \
            else 'unknown if alive or deceased'
        return a
    return author_json


class Musician(Author):
    """The class describing the concept of musician.
    It is assumed that a musician is sufficiently described as an Author, with addition of his/her
    music genre and instrument(s). These are defined as properties of the Musician class.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclass.
    """

    definition = 'Someone who plays music.'

    def __init__(self, name, birth_date=None, birth_place='unknown',
                 nationality='unknown', alive=Lives.ALIVE,
                 genre=Genre.ROCK,
                 instrument=Instrument.GUITAR):
        super().__init__(name, birth_date, birth_place,
                 nationality, alive)
        self.instrument = instrument
        self.genre = genre

    def __str__(self):
        return super().__str__() + str(self.instrument.name).lower() + ', ' + \
               str(self.genre)

    def __eq__(self, other):
        return super().__eq__(other) if other and isinstance(other, Musician) else False


class Poet(Author):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as an Author, with addition of
    the type of poetry they create. This is defined as a property of the Poet class.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclass.
    """

    definition = 'Someone who writes poetry.'

    def __init__(self, name, birth_date=None, birth_place='unknown',
                 nationality='unknown', alive=Lives.ALIVE,
                 poetry=PoetryType.LYRIC):
        super().__init__(name, birth_date, birth_place,
                 nationality, alive)
        self.poetry = poetry

    def __str__(self):
        return super().__str__() + str(self.poetry.name).lower() + ', '

    def __eq__(self, other):
        return super().__eq__(other) if other and isinstance(other, Poet) else False


class SingerSongwriter(Musician, Poet):
    """The class describing the concept of poet.
    It is assumed that a poet is sufficiently described as a Musician who is simultaneously a Poet.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also overrides the definition static field from the superclasses.
    """

    definition = 'Someone who plays music and writes poetry.'

    def __init__(self, name, birth_date=None, birth_place='unknown',
                 nationality='unknown', alive=Lives.ALIVE,
                 genre=Genre.ROCK,
                 instrument=Instrument.GUITAR,
                 poetry=PoetryType.LYRIC):
        # super().__init__(name, birth_date, birth_place,
        #          nationality, alive, genre, instrument)
        # super().__init__(name, birth_date, birth_place,
        #          nationality, alive, poetry)
        super().__init__(name)

    def __str__(self):
        return super().__str__()

    def __eq__(self, other):
        return super().__eq__(other)


if __name__ == "__main__":

    patti = Author("Patti Smith",
                   date(1946, 12, 30),
                   "Chicago",
                   "US")
    # print(patti)
    # print()
    #
    # Author.show_definition()
    # patti.show_definition()
    # print()
    #
    # bruce = Author.get_instance("Bruce Springsteen")
    # print(bruce)
    #
    # print(Author.alive_or_deceased(bruce))
    # print()
    #
    # bruce = Musician("Bruce Springsteen", date(1949, 9, 23), "Freehold", "US")
    # print(bruce)
    # print()
    #
    # patti = Poet('Patti Smith', date(1946, 12, 30), 'Chicago', 'US')
    # print(patti)
    # print()
    #
    # pattiSmith = SingerSongwriter('Patti Smith', date(1946, 12, 30), 'Chicago', 'US')
    # print(pattiSmith)
    # print()
    # print(SingerSongwriter.__mro__)
    # print()
    #
    #
    # patti.show_definition()
    # bruce.show_definition()
    # pattiSmith.show_definition()
    #
    # print()

    # patti_json = json.dumps(patti, indent=4, cls=AuthorEncoder)
    # print(patti_json)
    # print()
    #
    # pattiSmith = json.loads(patti_json, object_hook=json_to_py)
    # print(patti == pattiSmith)

    patti_json = jsonpickle.encode(patti)
    pattiSmith = jsonpickle.decode(patti_json)
    print(patti == pattiSmith)


