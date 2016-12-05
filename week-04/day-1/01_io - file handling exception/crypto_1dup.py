# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):

    decrypted = ""
    text = open(file_name, "r")
    encrypted = text.read()
    text.close()

    for lines in encrypted.splitlines():
        if len(lines) > 2:
            for i in range(0, len(lines), 2):
                decrypted += lines[i]
        decrypted += '\n'
    return decrypted

