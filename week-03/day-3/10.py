# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has


def mistery_triangle(lines):
    i = 1
    while i <= lines:
        print(" " * (lines - i), "*" * (i * 2 - 1))
        i += 1


mistery_triangle(10)