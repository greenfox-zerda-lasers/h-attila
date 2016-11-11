# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

list = [1, 2, [3, 4], 1, [1, [2, 4]]]



def rec_function(items):

#    print('ezzel fut:', items[0])
    print(items)

    if range(len(items)) :

        return 0

    else:

        if type(items[0]) == type([]):
            print('lista')
            return rec_function(items[0][0])

        else:
            print('nem lista')
            return items[0] + rec_function(items[1:])



print(rec_function(list))
