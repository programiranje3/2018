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


class PerformerEncoder(json.JSONEncoder):
    """JSON encoder for Performer objects.
    Redefines the default(self, o) method of json.JSONEncoder.
    """


def json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads()).
    """


if __name__ == "__main__":

    pass

