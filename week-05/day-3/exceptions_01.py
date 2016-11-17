# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def dividing_ten_by(number):

    try:
        return 10 / number
    except ZeroDivisionError:
        return('fail')
    except TypeError:
        return('fail')


print(dividing_ten_by('alma'))