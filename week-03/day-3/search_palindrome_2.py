# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['og go', ' dad ', 'd d', 'dood', 'eve']

# Inspirated by Endre



def search_palindrome(input_text):
    palindrome = []
    text = []

    for i in range(len(input_text)):
        for j in range(len(input_text)-i):
            text = input_text[i:j+1]
            if text == text[::-1] and len(text) >= 3:
                palindrome.append(text)
    print(palindrome)


search_palindrome('dog goat dad duck doodle never')