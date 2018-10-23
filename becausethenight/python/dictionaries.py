"""Demonstrates dictionaries
"""


def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - using the keys() and values() functions
    """

    d = {}
    d[1] = 'one'
    print(d)
    print(d[1])
    print()

    songs = {
        1: "Because the Night",
        2: "Dancing in the Dark",
        3: "You and I",
        4: "All of Us",
    }
    print(songs)
    print(songs.items())
    print(list(songs.items()))
    for k, v in songs.items():
        print(k, v)
    print()

    print(list(songs.keys()))
    print(list(songs.values()))
    print()


def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # if by == 'k':
    #     l = sorted(zip(d.keys(), d.values()))
    # elif by == 'v':
    #     l = sorted(zip(d.values(), d.keys()))
    # else:
    #     return(None)
    # return dict(l)

    from operator import itemgetter
    if by == 'k':
        l = sorted(d.items(), key=itemgetter(0))
    elif by == 'v':
        l = sorted(d.items(), key=itemgetter(1))
    else:
        return(None)
    return dict(l)


def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    songs = {
        11: "Because the Night",
        2: "Dancing in the Dark",
        31: "You and I",
        4: "All of Us",
    }

    print(songs.items())
    print(sort_dictionary(songs, 'k'))
    print(sort_dictionary(songs, 'v'))
    print(sort_dictionary(songs, 33))


if __name__ == '__main__':

    # demonstrate_dictionaries()
    demonstrate_dict_sorting()

