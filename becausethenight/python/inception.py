# print("Because the Night")
# print('Because the Night')
# print()
#
# print('Because the Night' + '\n' +
#       'is a legendary song :)')
# print()
#
# print('Because the Night' + '\n' +
#       'is a legendary song :) ' + str(1978))
# print('The song was first released in ' + str(1978))
# print('The song was first released in', 1978)

# print("Enter the release year for 'Because the Night': ", end='')
# year = input("Enter the release year for 'Because the Night': ")
# print('Year entered:', year)
#
# y = int(year)
# print(y)
#
# if y == 1978:
#     print("Because the Night")
# else:
#     print("Something else")
# print()


def print_b():
    print('Because the Night' + '\n' +
          'is a legendary song :)')
    print(__name__)
    print()


if __name__ == '__main__':

    for i in range(1, 5):
        print("Because the Night")

    print(__name__)

    print_b()


