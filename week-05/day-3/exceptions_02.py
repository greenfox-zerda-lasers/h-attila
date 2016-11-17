# write a function that takes a filename and returns the number of lines the
# file consists. It should return zero if the file not exists.


def magic_file_listener(filename):

    count =0

    try:
        my_file = open(filename, "r")
        my_data = my_file.readlines()
        my_file.close()

    except FileNotFoundError:
        return 0

    for i in my_data:
        count += 1
    return count


print(magic_file_listener('exceptions_02_data.txt'))