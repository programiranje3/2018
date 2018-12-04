"""Domain classes and functions related to the concept of performer
"""


import json

from becausethenight.util import utility


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


def py_to_json(performer):
    """JSON encoder for Performer objects (default= parameter in json.dumps()).
    """

    if isinstance(performer, Performer):
        return {'__Performer__': performer.__dict__}
    return {'__{}__'.format(performer.__class__.__name__): performer.__dict__}


class PerformerEncoder(json.JSONEncoder):
    """JSON encoder for Performer objects.
    Redefines the default(self, o) method of json.JSONEncoder.
    """

    def default(self, o):
        if isinstance(o, Performer):
            return {'__Performer__': o.__dict__}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


def json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads()).
    """

    if '__Performer__' in performer_json:
        p = Performer('')
        p.__dict__.update(performer_json['__Performer__'])
        return p
    return performer_json


if __name__ == "__main__":

    bruce = Performer("Bruce Springsteen")
    print(bruce)
    b = Performer("Bruce Springsteen")
    # print(b == bruce)
    print()

    # print(bruce.__class__)
    # print(bruce.__class__.__name__)
    # print(bruce.__dict__)

    # data_dir = utility.get_data_dir()
    # f = data_dir / 'bruce.json'
    #
    # with open(f, 'w') as jf:
    #     json.dump(bruce.__dict__, jf)
    # with open(f, 'r') as jf:
    #     br = json.load(jf)
    # print(br)
    # print()
    #
    # bruce_decoded = Performer('unknown', True)bruce_decoded = Performer('unknown', True)
    # print(bruce_decoded)
    # print(bruce_decoded.__dict__)
    # print()
    #
    # bruce_decoded.__dict__.update(br)
    # print(bruce_decoded)
    # print()

    # br_json = json.dumps(bruce.__dict__)
    # print(br_json)
    # print()
    #
    # bruce_decoded = Performer('unknown', True)
    # bruce_decoded.__dict__.update(json.loads(br_json))
    # print(bruce_decoded)

    # bruce_json = json.dumps(bruce, indent=4, default=py_to_json)
    bruce_json = json.dumps(bruce, indent=4, cls=PerformerEncoder)
    print(bruce_json)
    bruce_decoded = json.loads(bruce_json, object_hook=json_to_py)
    print(bruce == bruce_decoded)
    print()

