# Implement union method which combines two arrays.

array_1 = [4, 5, 7]
array_2 = [4, 1, 7]


def union_array(list1, list2):
    for item in list2:
        if item not in list1:
            list1.append(item)
            list1.sort()
    print(list1)



union_array(array_1, array_2)