numbers = [3, 4, 5, 6, 7]
numbers_2 = [3, 4, 5, 6, 7, 9, 11, 6, 5454545, 242355346246, 54435345435]

# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def even_list(input_numbers):
    result = []
    for i in input_numbers:
        if i % 2 == 0:
            result.append(i)
    print(result)

even_list(numbers)
even_list(numbers_2)



