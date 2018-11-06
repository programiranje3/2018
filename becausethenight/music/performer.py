"""Domain classes and functions related to the concept of performer
"""


import json


class Performer:
    """The class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether it is a solo performer or a band.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also defines the format_performer() method (converts a performer object to its name field for printing purposes).
    This can possibly be a static method.
    """

    def __init__(self, name, is_band=False):
        self.name = name
        self.is_band = is_band

    def __str__(self):
        return '{} ({})'.format(self.name, 'band' if self.is_band else 'solo performer')

    def __eq__(self, other):
        return (self.name == other.name and self.is_band == other.is_band) if isinstance(other, Performer) else False

    @staticmethod
    def format_performer(performer):
        return performer.name if isinstance(performer, Performer) else performer if isinstance(performer, str) else ''


class PerformerEncoder(json.JSONEncoder):
    """JSON encoder for Performer objects.
    Redefines the default(self, o) method of json.JSONEncoder.
    """


def json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    bruce = Performer("Bruce Springsteen")
    print(bruce)
    b = Performer("Bruce Springsteen")
    print(b == bruce)

