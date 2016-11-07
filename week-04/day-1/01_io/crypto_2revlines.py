# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):

    result = ''

    text = open(file_name, "r")
    reversed_line = text.read()
    text.close()

    for lines in reversed_line.splitlines():
        result += lines[::-1] + '\n'

    return(result)