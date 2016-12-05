# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):

    decrypted = ""
    text = open(file_name, "r")
    encrypted = text.read()
    text.close()

    for lines in encrypted.splitlines():
        for chars in lines:
            if chars != ' ':
                decrypted += chr(ord(chars) - 1)
            else:
                decrypted += ' '
        decrypted += '\n'

    return decrypted

