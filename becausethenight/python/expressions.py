"""Demonstrates how operators and expressions work in Python.
"""


# Demonstrate arithmetic operators (function demonstrate_arithmetic_operators())

def demonstrate_arithmetic_operators():
    a = ((7 // 3) ** 3) % 5 + 1
    print(a)

# Demonstrate relational operators (function demonstrate_relational_operators())
# - simple comparisons
# - comparing dates (== vs. is)
# - None in comparisons, type(None)


def demonstrate_relational_operators():
    if 2 > 3:
        print(True)
    else:
        print(False)

    # if 12:
    if None:
       print(True)
    else:
        print(False)
    print()

    print(type(None))
    print()

    from datetime import datetime, date, timedelta
    d1 = date.today()
    print(d1)
    d2 = date.today() - timedelta(1)
    print(d2)
    print()

    print(d1 > d2)
    print(d1 == d2)
    print()

    d2 = date.today()
    print(d1 is d2)
    print('id(d1):', id(d1), 'id(d2)', id(d2))
    d2 = d1
    print('id(d1):', id(d1), 'id(d2)', id(d2))
    a = '12'
    b = '12'
    print(a is b)


# Demonstrate logical operators (function demonstrate_logical_operators())
# - logical operations with True and False
# - logical operations with dates
# - logical operations with None (incl. None and int, None and date, etc.)
# - None and date vs. None > date

def demonstrate_logical_operators():
    print(True and False)
    print(True or False)
    print()

    from datetime import datetime, date, timedelta
    d1 = date.today()
    print(d1 and True)
    print(0 and True)
    print(d1 and False)
    print(d1 and None)


if __name__ == '__main__':

    # demonstrate_arithmetic_operators()
    # demonstrate_relational_operators()
    demonstrate_logical_operators()

