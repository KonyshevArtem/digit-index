import unittest
from digit_index import get_digit_one_based, get_digit_zero_based


class DigitsIndexTests(unittest.TestCase):
    def test_0_should_be_on_index_0(self):
        digit = get_digit_zero_based(0)
        self.assertEqual(0, digit)

    def test_1_should_be_on_index_1(self):
        digit = get_digit_zero_based(1)
        self.assertEqual(1, digit)

    def test_0_should_be_on_index_11(self):
        digit = get_digit_zero_based(11)
        self.assertEqual(0, digit)

    def test_1_based_index(self):
        digit_zero_based = get_digit_zero_based(50)
        digit_one_based = get_digit_one_based(49)
        self.assertEqual(digit_one_based, digit_zero_based)


if __name__ == '__main__':
    unittest.main()
