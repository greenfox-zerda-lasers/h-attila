import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    # Adds a and b, returns as result
    def test_add_1_and_2_is_3_my(self):
        self.assertEqual(extend.add(1, 2), 3)

    def test_add_1_and_minus_1_is_0_my(self):
        self.assertEqual(extend.add(1, -1), 0)


    # Returns the highest value from the three given params
    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(3, 4, 2), 4)


    def test_max_of_three_third_my(self):
        self.assertEqual(extend.max_of_three(4, 3, 5), 5)


    # Returns the median value of a list given as param
    def test_median_four(self):
        self.assertEqual(extend.median([7,5,4,1]), 4.5)

    def test_median_five(self):
        self.assertEqual(extend.median([0,2,3,4,10]), 3)


    # Returns true if the param is a vovel
    def test_is_vovel_a(self):
        self.assertTrue(extend.is_vovel('a'))

    def test_is_vovel_u(self):
        self.assertTrue(extend.is_vovel('ú'))


    # Create a method that translates hungarian into the teve language
    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('bemutaatkozik'), 'bevemuvutavaavatkovozivik')

    def test_translate_kolbice(self):
        self.assertEqual(extend.translate('kolbice'), 'kovolbiviceve')

if __name__ == '__main__':
    unittest.main()