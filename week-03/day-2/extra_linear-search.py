# linear search
# return number's place in the table, if not found: '-1'

list = [4,5,6]
number = 6


def linear_search(input_list, searched_number):
    result = -1
    found = False
    for i in input_list:
        result += 1
        if searched_number == i:
            found = True
            break
    if found:
        print("Az eredmeny:", result)
    else:
        print("-1")

linear_search(list, number)
