numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def reverse_list(list):
    newlist = []
    for i in list[::-1]:
        newlist.append(i)
    print(newlist)


reverse_list(numbers)