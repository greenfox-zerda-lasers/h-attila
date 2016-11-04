# create a function that takes a list and returns a new list with all the elements doubled

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def list_dubler(list):
    for i in range(len(list)):
        print(i)
        list[i] *= 2
    return list


print(list_dubler(data))
