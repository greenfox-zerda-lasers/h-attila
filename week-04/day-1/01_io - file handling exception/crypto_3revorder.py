# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):

    result = ''

    text = open(file_name, "r")
    reversed_line = text.read()
    text.close()

    for lines in reversed_line.splitlines()[::-1]:
        result += lines + '\n'

    return(result)
