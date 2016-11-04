names = ['Zakarias', 'Hans', 'Otto', 'Ole']
# create a function that returns the shortest string
# from a list


def shortest_names(input):
    shortest = input[0]
    for i in input:
        if len(i) < len(shortest):
            shortest = i
    print("Shortest word is:", shortest)


shortest_names(names)