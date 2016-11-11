# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def magic_string(string):

    if len(string) < 1:
        return ''
    else:
        if string[0] == 'x':
            return '' + magic_string(string[1:])
        else:
            return string[0] + magic_string(string[1:])


print(magic_string('xaxaxaxaxa'))