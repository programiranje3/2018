"""Demonstrates pass, returning None, functions as parameters of other functions,
functions as return values of other functions and user-defined decorators
"""


import functools


def return_none():
    """Demonstrates returning None and the pass statement.
    """

    pass


def pass_function_as_parameter(f, *args):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    """

    f(*args)


def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    In this example, depending on the first_name_flag, return_function() returns one of the following functions:
    - a function that returns a person's first name
    - a function that returns a person's family name
    """

    def first():
        return full_name.split()[0]

    def second():
        return full_name.split()[1]

    return first if first_name_flag else second

def return_function_with_args(*args):
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    In this example, depending on len(args), return_function_with_args() returns one of the following functions:
    - a function that returns an empty list
    - a function that returns a tuple of args (or a list or args, or...)
    """

    def empty():
        return []

    def with_args(*p):
        return tuple(p)

    return with_args if len(args) else empty


def show_author(artwork_f):
    """Demonstrates how to develop a decorator. Uses the decorator-writing pattern:
    import functools
    def decorator(func):
        @functools.wraps(func)			                # preserves func's identity after it's decorated
        def wrapper_decorator(*args, **kwargs):
            # Do something before
            value = func(*args, **kwargs)
            # Do something after
            return value
        return wrapper_decorator
    """

    @functools.wraps(artwork_f)
    def wrap_artwork_f(*args, **kwargs):
        """Wrapper"""

        authors = list(args)
        del authors[0]
        print(', '.join(a for a in authors), ':', end='')

        v = artwork_f(*args, **kwargs)

        print(':)')

        return v

    return wrap_artwork_f


@show_author
def print_song(title, *authors):
    """The corresponding decorator (@show_author); omit it if decorating manually.
    """

    print(title)


if __name__ == '__main__':

    print(return_none())
    print(type(return_none()))
    print()

    from becausethenight.python.functions import show_song

    pass_function_as_parameter(show_song, 'Bruce')
    print()

    f = return_function("Patti Smith", 34)
    print(f)
    print(f())
    print()

    f = return_function_with_args(1)
    print(f)
    print(f('Bruce', 'Patti'))
    f = return_function_with_args()
    print(f())
    g = f
    print(g())
    print()

    print_song("Because the Night", "Bruce", "Patti")
    print()

    # f = show_author(print_song)
    # f("Because the Night", "Bruce", "Patti")

    # print_song = show_author(print_song)
    # print_song("Because the Night", "Bruce", "Patti")
    print_song("Because the Night", "Bruce", "Patti")
    print(print_song.__name__)
    print(print_song.__doc__)
