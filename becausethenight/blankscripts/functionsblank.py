"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


def demonstrate_annotations(artist: str, song: str = 'Because the Night') -> str:
    """Demonstrates how to use annotations of function parameters/arguments and of function return type.
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - return a formatted string (including function parameters/arguments)
    """


def show_song(artist, song='Because the Night', duration=180):
    """Demonstrates default arguments/parameters.
    - print the function arguments/parameters in one line
    """


def use_flexible_arg_list(prompt: str, *songs):
    """Demonstrates flexible number of arguments/parameters.
    - print the prompt and the list of songs in one line
    """


def use_all_categories_of_args(prompt, *albums, song='Because the Night', **authors):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """


if __name__ == "__main__":
    pass


