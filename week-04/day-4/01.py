# 1. write a recursive function
# that takes one parameter: n
# and counts down from n


def magic_factorial(n):

    print(n)

    if n > 0:
        magic_factorial(n-1)


magic_factorial(5)
