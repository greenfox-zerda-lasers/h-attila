# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has


def mistery_diamond(lines):
    i = 1
    j = 1
    direction = 1

    while j <= (lines * 2):
        print(" " * (lines - i), "*" * (i * 2 - 1), " " * (lines * 2 - i * 2), "*" * (i * 2 -1), " " * (lines * 2 - i * 2), "*" * (i * 2 - 1), " " * (lines * 2 - i * 2), "*" * (i * 2 -1), " " * (lines * 2 - i * 2), "*" * (i * 2 - 1), " " * (lines * 2 - i * 2), "*" * (i * 2 -1), " " * (lines * 2 - i * 2), "*" * (i * 2 - 1), " " * (lines * 2 - i * 2), "*" * (i * 2 -1), " " * (lines * 2 - i * 2), "*" * (i * 2 -1), " " * (lines * 2 - i * 2), "*" * (i * 2 -1))
        i += direction
        j += 1
        if i == lines:
            direction = -1



mistery_diamond(10)