# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".


def magic_string(string):

    if len(string) <= 1:
        return string[0]
    else:
        return string[0] + '*' + magic_string(string[1:])


print(magic_string('1234567890'))