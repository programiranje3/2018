"""Demonstrates working with strings in Python.
"""

import string


def demonstrate_formatting():
    """Using classical formatting.
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    print('%7.2f %s' % (45/34, 'eee'))
    print('C:\nowhere')
    print(r'C:\nowhere')
    print("""Songs
        'Because the Night'
        'Space Monkey
    """)
    print('Because the Night   ' * 3)
    b = list('Because the Night')
    print(b)
    print(b[0:7])
    print(b[-5:])
    print()

    print(str(4.5))
    print(repr(4.5))
    print()

    print(string.whitespace)
    print(str(string.whitespace))
    print(repr(string.whitespace))


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('{0}, {1} ({2})'.format("Because the Night", 1978, "Patti Smith"))
    print('{1}, {0} ({2})'.format("Because the Night", 1978, "Patti Smith"))


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals(), len(),...)
    """

    song = "Because the Night"
    print(song.endswith('Night'))
    print('the' in song)
    print(song.split())
    print(song.center(30, '#'))


if __name__ == '__main__':

    # demonstrate_formatting()
    # demonstrate_fancy_formatting()
    demonstrate_string_operations()
