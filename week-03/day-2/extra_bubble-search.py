bubble = [9, 1, 2, 3, 4, 5]


# Implement binary search, wich tests if the param is sorted, sorts if not and search for the other param.

def bubble_search(list):
    change = True
    j = 1

    while j in range(len(list)):
        i = 0
        while i in range(len(list) - j):
            if list[i] > list[i + 1]:
                # ha van csere
                list[i], list[i + 1] = list[i + 1], list[i]
                change = True
            else:
                # ha nincsen csere
                change = False
            print(list)
            i += 1
        if change == False:
            break
        j += 1


bubble_search(bubble)
