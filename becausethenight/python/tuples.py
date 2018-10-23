"""Demonstrates tuples
"""


def demonstrate_tuples():
    """Creating and using tuples.
    - create and print 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    t1 = (1, )
    t2 = (1, 2)
    t4 = ("Bruce", "Patti", 1978, True)
    print(t1, t2, t4)
    print(t4[1])
    print(id(t1))
    t1 = t1 + t4
    print(id(t1))
    print(t1)
    print()

    print()


def demonstrate_zip():
    """Using the built-in zip() function with tuples and double-counter for-loop.
    """

    t1 = ("Bruce", "Patti", 1978)
    t2 = ("Springsteen", "Smith", "Because the Night")
    z = zip(t1, t2)
    print(z)
    print(list(z))
    for i, j in z:
        print(i, j)


def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    t1 = ("Bruce", "Patti", 1978)
    bruce, patti, year = t1
    all = bruce, patti, year
    print(bruce, patti, year)
    print("All: " + str(all))
    print()


if __name__ == '__main__':

    # demonstrate_tuples()
    # demonstrate_zip()
    demonstrate_packing()


