# Implement binary search, wich tests if the param is sorted, sorts if not and search for the other param.

data = [1, 21, 3, 44, 51, 64, 7, 8567, 9, 13450, 454, 34534, 43, 54, 23, 76, 547, 23, 3465, 456, 124, 678, 2346, 2424, 7531]
searched_number = 54


def binary_search(list, number):

    # checking list is sorted or not
    if list == sorted(list):
        print("sorted")
    else:
        print("not sorted, sorting ...")
        list.sort()
        print("sorted list is:", list)

    # checking searched number is in the list range
    if list[0] > number or list[len(list)-1] < number:
        print("Not in list's range!")
    else:
        # start searching in list
        is_found = False
        pos_min = 0
        pos_max = len(list)

        while not is_found:
            pos_act = int((pos_max + pos_min) / 2)
            print("Not found. Pos min:", pos_min, "pos max:", pos_max, "pos act:", pos_act)

            if number == list[pos_act]:
                is_found = True
                break
            elif number < list[pos_act]:
                pos_max = pos_act-1
            else:
                pos_min = pos_act+1

            # searched number not in list
            if pos_act == pos_min and pos_act == pos_max:
                break

        if is_found:
            print("Hurray,", number, "found in position:", pos_act)
        else:
            print("Not found in the list...")


binary_search(data, searched_number)
