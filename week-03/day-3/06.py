# create a function that takes a list and returns a new list that is reversed


def magic_reverse(input_list):
    newlist = []
    for i in range(len(input_list)):
        print(i, len(input_list))
        newlist.append(input_list[len(input_list)-1-i])
    print(newlist)


list = [1, 2, 3, 4, 99]

magic_reverse(list)