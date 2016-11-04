# Implement union method which combines two arrays.

array_1 = [4, 5, 7]
array_2 = [4, 1, 7]


def union_array(input_array_1, input_array_2):
    result = input_array_1
    for i in range(len(input_array_1)):
        if input_array_1[i] in array_2:
            continue
        else:
            result.append(input_array_2[i])
    result.sort()
    print(result)


union_array(array_1, array_2)