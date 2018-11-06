"""Domain classes and functions related to the concept of album
"""


from classes2018.util import utility


class Album:
    """The class describing the concept of album.
    It is assumed that an album is sufficiently described by its
    title, performer, songs, duration and release date.
    The class defines the __init__(), __str__(), __eq__(), __iter__() and __next__() methods.
    """


def format_songs(songs):
    """Formats the album's song list for __str__().
    """


def generate_songs(songs):
    """A generator of Song objects, given the input list of songs.
    """


class AlbumError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class SongNotIncludedError(AlbumError):
    """Exception raised when a song from an album is requested,
    but is not included in the list of songs from that album.
    """


def play_song(song, album):
    """Play the requested song from the album.
    Raises SongNotIncludedError() if the requested song is not included on the album.
    """


if __name__ == "__main__":

    pass

