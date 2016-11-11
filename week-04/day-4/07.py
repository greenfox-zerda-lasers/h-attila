# 7. Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def magic_string(string):

    if len(string) < 1:
        return ''
    else:
        if string[0] == 'x':
            return 'y' + magic_string(string[1:])
        else:
            return string[0] + magic_string(string[1:])


print(magic_string('xaXxxxxxx'))