import unittest
from exceptions_01 import *

class the_big_test(unittest.TestCase):

    def test_the_normal_work(self):
        self.assertEqual(dividing_ten_by(1), 10.0)

    def test_divide_by_zero(self):
        self.assertEqual(dividing_ten_by(0), 'fail')

    def test_none_numeric_input(self):
        self.assertEqual(dividing_ten_by('alma'), 'fail')



if __name__ == '__main__':
    unittest.main()