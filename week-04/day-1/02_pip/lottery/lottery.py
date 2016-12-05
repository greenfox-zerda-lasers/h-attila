# Create a method that returns the five most frequent lottery number in a pretty table format

from collections import Counter


def five_most_frequent():

    numbers = []

    data_from_file = open("otos.csv", "r")
    lines = data_from_file.readlines()
    data_from_file.close()

    for items in lines:
        numbers += items.rstrip().split(';')[-5::]
    counted_numbers = Counter(numbers)
    print(counted_numbers.most_common()[:5:])




five_most_frequent()
