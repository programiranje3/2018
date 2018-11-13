"""Domain classes and functions related to the concept of album
"""
import datetime

from becausethenight.music.author import Author
from becausethenight.music.performer import Performer
from becausethenight.music.song import Song
from becausethenight.util import utility


class Album:
    """The class describing the concept of album.
    It is assumed that an album is sufficiently described by its
    title, performer, songs, duration and release date.
    The class defines the __init__(), __str__(), __eq__(), __iter__() and __next__() methods.
    """

    def __init__(self, title, performer=None, songs=None, duration=0, release_date=None):
        self.title = title
        self.performer = performer
        self.songs = songs
        self.duration = duration
        self.release_date = release_date

        self.__i = 0

    def __str__(self):
        s = self.title + '\n' + '\tperformer: {}\n\tsongs:\n\t\t{}' + \
               '\n\tduration: {}\n' + '\trelease date: {}\n'
        return s.\
            format(Performer.format_performer(self.performer),
                   format_songs(self.songs),
                   utility.format_duration(self.duration),
                   utility.format_date(self.release_date))

    def __eq__(self, other):
        return self.title == other.title and self.performer == other.performer \
            if other and isinstance(other, Album) else False

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i < len(self.songs):
            song = self.songs[self.__i]
            self.__i += 1
            return song
        else:
            raise StopIteration


def format_songs(songs):
    """Formats the album's song list for __str__().
    """

    return '\n\t\t'.join([s.title for s in songs]) if songs and isinstance(songs, list) \
        else 'not specified'


def shuffle(album, seed, play_time):
    """A generator of song titles from a given album in random order.
    Simulates shuffle-playing of songs from the album
    for play_time time (a float number expected by time.perf_counter()).
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

    patti_smith = Performer('Patti Smith')
    bruce_springsteen = Author('Bruce Springsteen', datetime.date(1949, 9, 23), 'Freehold',
                               'US')
    because_the_night = Song('Because the Night',
                             patti_smith,
                             bruce_springsteen,
                             183,
                             datetime.date(1978, 3, 3))
    rockNroll_nigger = Song("Rock 'n' Roll Nigger",
                             patti_smith,
                             bruce_springsteen,
                             215,
                             datetime.date(1978, 3, 3))
    twenty_fifth_floor = Song('25th Floor',
                             patti_smith,
                             bruce_springsteen,
                             199,
                             datetime.date(1978, 3, 3))

    easter = Album('Easter', patti_smith,
                   [because_the_night, rockNroll_nigger, twenty_fifth_floor],
                   10000,
                   datetime.date(1978, 3, 3))

    print(easter)
