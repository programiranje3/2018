"""Domain classes and functions related to the concept of album
"""


import datetime
import random
import sys
from time import perf_counter

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

    random.seed(seed)
    play_until = perf_counter() + play_time
    i = random.randint(0, len(album.songs) - 1)
    while perf_counter() < play_until:
        yield album.songs[i].title
        i = random.randint(0, len(album.songs) - 1)


class AlbumError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class SongNotIncludedError(AlbumError):
    """Exception raised when a song from an album is requested,
    but is not included in the list of songs from that album.
    """

    def __init__(self, song, album):
        self.song = song
        self.album = album
        self.message = 'Song {} not on album {}'.format(song.title, album.title)


def play_song(song, album):
    """Play the requested song from the album.
    Raises SongNotIncludedError() if the requested song is not included on the album.
    """

    if isinstance(album, Album) and isinstance(song, Song):
        if song in album.songs:
            print(song.title)
        else:
            raise SongNotIncludedError(song, album)
    else:
        raise TypeError()



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
    dancing_barefoot = Song('Dancing barefoot', patti_smith)

    easter = Album('Easter', patti_smith,
                   [because_the_night, rockNroll_nigger, twenty_fifth_floor],
                   10000,
                   datetime.date(1978, 3, 3))

    print(easter)
    print()

    # for title in shuffle(easter, 23, 0.001):
    #     print(title)
    # print()

    # try:
    #     twenty_fifth_floor / 2
    # except:
    #     # print('exception caught')
    #     sys.stderr.write('exception caught')

    songs = [because_the_night, rockNroll_nigger, twenty_fifth_floor]
    # for i in range(5):
    #     try:
    #         print(songs[i].title)
    #         # twenty_fifth_floor / 2
    #     except IndexError as e:
    #         print(e.args)
    #         print(e.args[0])
    #         break
    #     except Exception as e:
    #         # print('exception caught')
    #         # sys.stderr.write('exception caught')
    #         print()
    #         print(type(e).__name__)
    #         print(e.__class__.__name__)
    #         break
    #     else:
    #         print("Nice song...")
    #     finally:
    #         print("Done.")

    try:
        # play_song(because_the_night, easter)
        play_song(dancing_barefoot, easter)
    except TypeError as e:
        print(e.args[0])
    except SongNotIncludedError as e:
        print(e.message)
        # print(e.args)
    else:
        print("Nice song...")
    finally:
        print('Done.')


