"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


def demonstrate_annotations(artist: str, song: str = 'Because the Night') -> str:
    """Demonstrates how to use annotations of function parameters/arguments and of function return type.
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - return a formatted string (including function parameters/arguments)
    """
    print('P:', 'artist:', artist, 'song:', song)
    print('A:', demonstrate_annotations.__annotations__)
    return artist + ': ' + song


def show_song(artist, song='Because the Night', duration=180):
    """Demonstrates default arguments/parameters.
    - print the function arguments/parameters in one line
    """

    print(artist, song + ' (' + str(duration) + ')')


def use_flexible_arg_list(prompt: str, *songs):
    """Demonstrates flexible number of arguments/parameters.
    - print the prompt and the list of songs in one line
    """

    print(prompt + ':', ', '.join(s for s in songs))


def use_all_categories_of_args(prompt, *albums, song='Because the Night', **authors):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    print(song + ':', ', '.join(a for a in albums), ';', ', '.join(a for a in authors.values()))


if __name__ == "__main__":

    # demonstrate_annotations(1, 'Frederick')
    print(demonstrate_annotations('Patti', 'Frederick'))
    print()

    show_song('Bruce')
    show_song('Bruce', song='Downbound Train', duration=234)
    show_song(artist='Bruce', song='Downbound Train', duration=234)
    # show_song(artist='Bruce', 'Downbound Train', duration=234)
    print()

    use_flexible_arg_list('Songs', 'Dancing in the Dark', 'Born in the USA', 'Brilliant Disguise')
    use_flexible_arg_list('Songs')
    print()

    albums = ['Easter', 'Promise', 'Best Of']
    authors = {
        # 'a1': 'Bruce Springsteen',
        'a2': 'Patti Smith',
    }
    use_all_categories_of_args('Songs', 'Easter', 'Promise',
                               a1='Bruce Springsteen',
                               a2='Patti Smith')
    use_all_categories_of_args('Songs', *albums, **authors)
    print()


