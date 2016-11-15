# Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.


def anagramm(text_a, text_b):
    return sorted(text_a.lower().replace(" ", "")) == sorted(text_b.lower().replace(" ", ""))


def count_letters(text):
    text = text.lower()
    result = {}
    for i in text:
        if i.isalpha():
            if i in result:
                result[i] += 1
            else:
                result[i] = 1
    return result