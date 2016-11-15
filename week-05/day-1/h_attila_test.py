import unittest
from h_attila_work import *


class Anagramm_The_Big_Test(unittest.TestCase):

    # --- Anagramm testing ---

    def test_normal_function(self):
        self.assertTrue(anagramm('alma', 'aalm'))

    def test_with_different_strings(self):
        self.assertFalse(anagramm('alma', 'korte'))

    def test_with_accent_marks(self):
        self.assertTrue(anagramm('béla', 'élab'))

    def test_extra_space(self):
        self.assertTrue(anagramm('alma', 'al ma'))

    def test_with_different_length_strings(self):
        self.assertFalse(anagramm('alma', 'almaa'))

    def test_lowercase_uppercase_strings(self):
        self.assertTrue(anagramm('alma', 'ALMA'))

    def test_with_text_numbers(self):
        self.assertFalse(anagramm('alma', '1234'))

    def test_with_numeric_numbers(self):
        self.assertRaises(AttributeError, anagramm, 'alma', 1234)


class Count_Letter_Test(unittest.TestCase):

    # --- Count Letter testing ---

    def test_normal_function(self):
        self.assertEqual(count_letters('aaaabbbccd'), {'b': 3, 'd': 1, 'c': 2, 'a': 4})

    def test_upper_lower_letters(self):
        self.assertEqual(count_letters('aAAabBbcCd'), {'b': 3, 'd': 1, 'c': 2, 'a': 4})

    def test_normal_function_with_space(self):
        self.assertNotEqual(count_letters('aaaa bbb cc d'), {' ': 3, 'b': 3, 'd': 1, 'c': 2, 'a': 4})

    def test_spaces_missing(self):
        self.assertNotEqual(count_letters('aaaa bbb cc d'), {'b': 4, 'd': 3, 'c': 2, 'a': 1})

    def test_with_invalid_characters(self):
        self.assertEqual(count_letters(',.-?:_+!%/='), {})

    def test_with_not_string_input(self):
        self.assertRaises(AttributeError, count_letters, 123)

    def test_with_empty_string(self):
        self.assertEqual(count_letters(''), {})

    def test_with_some_accent_marks(self):
        self.assertEqual(count_letters('aáeéiíoöőuúüű'), {'á': 1, 'i': 1, 'e': 1, 'ű': 1, 'ő': 1, 'ú': 1, 'ü': 1, 'o': 1, 'u': 1, 'ö': 1, 'é': 1, 'a': 1, 'í': 1})


if __name__ == '__main__':
    unittest.main()