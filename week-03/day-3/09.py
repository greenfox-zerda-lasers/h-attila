# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

def triangle(lines):
    i = 1
    while i <= lines:
        print("*" * i)
        i +=1



triangle(2)
triangle(4)
triangle(6)
triangle(8)
triangle(10)
