# this function creates palindromes from input text

def create_palindrome(text):
    return text + text[::-1]

print(create_palindrome('alma'))