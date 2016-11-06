# this function creates palindromes from input text

def create_palindrome(text):
    palindrome = text
    for i in range(len(text)):
        palindrome += text[len(text)-1-i]
    return palindrome

print(create_palindrome('alma'))