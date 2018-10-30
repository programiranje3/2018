"""Demonstrates pass, returning None, functions as parameters of other functions,
functions as return values of other functions and user-defined decorators
"""


import functools


def return_none():
    """Demonstrates returning None and the pass statement.
    """


def pass_function_as_parameter(f, *args):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    """


def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    In this example, depending on the first_name_flag, return_function() returns one of the following functions:
    - a function that returns a person's first name
    - a function that returns a person's family name
    """


def return_function_with_args(*args):
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    In this example, depending on len(args), return_function_with_args() returns one of the following functions:
    - a function that returns an empty list
    - a function that returns a tuple of args (or a list or args, or...)
    """


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


@show_author
def print_song(title, *authors):
    """The corresponding decorator (@show_author); omit it if decorating manually.
    """


if __name__ == '__main__':

    from classes2018.python import functions


