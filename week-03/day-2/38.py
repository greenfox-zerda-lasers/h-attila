numbers = [7, 5, 8, -1, 2]


# Write a function that returns the minimal element
# in a list (your own min function)

def minimal(input):
    result = input[0]
    for i in input:
        if i < result:
            result = i
    print("Minimal number is:", result)


minimal(numbers)
