"""Demonstrates sets
"""


def demonstrate_sets():
    """Creating and using sets.
    - create a set with an attempt to duplicate items
    - demonstrate some of the typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    s = {"Bruce Springsteen", "Patti Smith", "Bruce Springsteen", "Foy Vance"}
    s1 = {"Bruce Springsteen", "Patti Smith", "Eric Clapton"}
    print(s)
    print(s & s1)
    print(s | s1)
    print(s - s1)
    print(s ^ s1)
    print()

    print()


if __name__ == '__main__':
    demonstrate_sets()

