import unittest
from exceptions_02 import *

class My_super_tests((unittest.TestCase)):

    def test_normal_working(self):
        self.assertEqual(magic_file_listener('exceptions_02_data.txt'), 8)

    def test_file_not_found(self):
        self.assertEqual(magic_file_listener('no_file_this_name.txt'), 8)


if __name__ == '__main__':
    unittest.main()