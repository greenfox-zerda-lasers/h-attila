# this function search and print the palindromes from the input text

def search_palindromes(text):
    range = 1
    akt_pos = 1
    new_palindrome = ''
    palindrome = []

    while akt_pos < len(text) - 1:

        found = True

        while found:
            # check we're in the string
            if (akt_pos - range) >= 0 and (akt_pos + range) < (len(text)):

                # searching for odd strings, like 'aba', 'abcba'
                if text[akt_pos - range : akt_pos] == text[akt_pos + range : akt_pos : -1]:
                    # found one!
                    new_palindrome = text[akt_pos - range : akt_pos + range + 1]
                    range += 1

                # searching for even strings, like 'abba', 'abccba'
                elif text[akt_pos - range : akt_pos +1] == text[akt_pos + range +1 : akt_pos : -1]:
                    # found one!
                    new_palindrome = text[akt_pos - range:akt_pos + range + 2]
                    range += 1

                else:
                    # not found
                    found = False
                    range = 1

            # text out of range
            else:
                found = False

        # add the new found palindrome to the list
        if new_palindrome != '':
            palindrome.append(new_palindrome)
            new_palindrome = ''

        # one step right
        akt_pos += 1

    return palindrome



output = search_palindromes('dog goat dad duck doodle never')
print(output)
