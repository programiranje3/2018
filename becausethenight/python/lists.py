"""Demonstrates working with lists.
"""


def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    l1 = ["Patti Smith", 1978, True, "Bruce Springsteen", 189.78]
    print(l1)
    print(l1[-2:])
    print()

    l2 = ["Patti Smith", 1978, True, "Bruce Springsteen", 189.78]
    print(l1 == l2)
    print(l1 is l2)

    print(l2 + ["Lenny Kaye"])
    l3 = ["Lenny Kaye"]
    l2.append(l3)
    print(l2)


def demonstrate_list_methods():
    """Using append(), insert(), remove(), pop(), extend(),
    count(), index(), reverse(), len(),...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    l1 = ["Because the Night", "You and I", "Love"]
    print(l1)
    print()

    l1.append("I'm on Fire")
    print(l1)
    print()

    # l1.extend(str(123))
    # l1.extend("Make It Rain")
    l1.extend(["Make It Rain"])     # same as l1 + ["Make It Rain"]
    print(l1)
    print()

    l2 = l1 + ["Clapton"]
    print(l2)
    print()

    l1.insert(0, "Layla")
    print(l1)
    print()

    l1.remove('3')
    print(l1)
    print()

    two = l1.pop(len(l1) - 1)
    print(two)
    print()

    l1.append("Layla")
    print(l1)
    print(l1.count("Layla"))
    print()

    print(l1.index("You and I"))
    print()

    l1.reverse()
    print(l1)
    print()
    print(l1.reverse())
    print()

    if "I'm on Fire" in l1:
        print(True)
    else:
        print(False)
    print()

    if "You Are So Beautiful Tonight" not in l1:
        print(True)
    else:
        print(False)
    print()


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array

    v = array('i', [12, 13, 14])
    print(type(v))

    l = [12, 13, 14]
    print(type(l))

    print(v[0])


def populate_empty_list():
    """Creating an empty list and populating it with random values."""

    import random
    l = []

    random.seed(234)
    for i in range(1, 1000):
        l.append(random.randint(1, 1234))
    print(l[0:10])
    print()


def duplicate_list():
    """Duplicating lists (carefully :))"""

    l1 = ["Because the Night", "You and I", "Love"]
    l2 = l1
    l2 = l1.copy()
    l3 = l1 + []
    l4 = l1[:]

    all = [l1, l2, l3, l4]
    for l in all:
        print(str(id(l)) + ": " + str(l))


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    Using str() and join() in printing results.
    """

    songs = ["We Are The Champions", "Love You To", "You And I"]
    print(' '.join([title.split()[0] for title in songs]))


if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    duplicate_list()
    # demonstrate_arrays()
    # populate_empty_list()
    # demonstrate_list_comprehension()


