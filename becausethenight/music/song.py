"""Domain classes and functions related to the concept of song
"""
from becausethenight.music.performer import Performer
from becausethenight.util import utility
from becausethenight.music.author import Author

from datetime import date
import pickle


class Song:
    """The class describing the concept of song.
    It is assumed that a song is sufficiently described by its
    title, performer, author, duration and release date.
    The class defines the __init__(), __str__() and __eq__() methods.
    It also defines the play() method that "plays" the corresponding song.
    """

    def __init__(self, title, performer=None, author=None, duration=0, release_date=None):
        self.title = title
        self.performer = performer
        self.author = author
        self.duration = duration
        self.release_date = release_date

    def __str__(self):
        # return self.title + ', ' + str(self.performer) + ', ' + \
        return self.title + ', ' + Performer.format_performer(self.performer) + ', ' + \
               str(self.author) + ', ' + str(self.duration) + ', ' + \
               str(self.release_date)

    def __eq__(self, other):
        # return True if isinstance(other, Song) and self.title == other.title and self.performer == other.performer else False
        return isinstance(other, Song) and self.title == other.title and self.performer == other.performer

    def play(self):
        print(self.title + ': ' + Performer.format_performer(self.performer))


if __name__ == "__main__":

    because_the_night = Song("Because the Night",
                             "Patti",
                             "Bruce and Patti",
                             200,
                             date(1978, 3, 2))
    # b = Song("Because the Night",
    #          "Patti",
    #          "Bruce Springsteen and Patti Smith",
    #          200,
    #          date(1978, 3, 2))
    # print(because_the_night)
    # print(because_the_night == b)
    # print()
    #
    # patti = Performer("Patti Smith")
    # because_the_night.play()
    # print()
    #
    # because_the_night.performer = patti
    # because_the_night.play()

    # with open('because_the_night.txt', 'w') as f:
    #     f.write(str(because_the_night))
    # with open('because_the_night.txt', 'r') as f:
    #     btn = f.read()
    # print(str(because_the_night) == btn)
    # print()

    # with open('because_the_night', 'wb') as f:
    #     f.write(str.encode(str(because_the_night)))
    # with open('because_the_night', 'rb') as f:
    #     btn = f.read()
    # print(btn)
    # print(str(because_the_night) == btn.decode())
    # print()

    # data_dir = utility.get_data_dir()
    # print(data_dir)
    # print()
    #
    # f = data_dir / 'because_the_night'
    # f.write_text(str(because_the_night))
    #
    # btn = f.read_text()
    # print(str(because_the_night) == btn)
    data_dir = utility.get_data_dir()
    f = data_dir / 'because_the_night'


    # with open(f, 'wb') as jf:
    #     pickle.dump(because_the_night, jf, protocol=pickle.HIGHEST_PROTOCOL)
    # print('Pickled.')
    # print()
    #
    # with open(f, 'rb') as jf:
    #     b = pickle.load(jf)
    # print(b == because_the_night)

    because_the_night_pickled_s = \
        pickle.dumps(because_the_night, protocol=pickle.HIGHEST_PROTOCOL)
    b = pickle.loads(because_the_night_pickled_s)
    print(b == because_the_night)



