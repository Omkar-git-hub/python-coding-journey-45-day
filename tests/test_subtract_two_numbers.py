import unittest
from subtract_two_numbers import subtract_two_numbers

class TestSubtractTwoNumbers(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(subtract_two_numbers(10, 5), 5)

    def test_subtract_negative_result(self):
        self.assertEqual(subtract_two_numbers(5, 10), -5)

    def test_subtract_with_zero(self):
        self.assertEqual(subtract_two_numbers(5, 0), 5)
        self.assertEqual(subtract_two_numbers(0, 5), -5)

    def test_subtract_negative_numbers(self):
        self.assertEqual(subtract_two_numbers(-5, -10), 5)
        self.assertEqual(subtract_two_numbers(-10, -5), -5)

    def test_subtract_floats(self):
        self.assertAlmostEqual(subtract_two_numbers(10.5, 5.2), 5.3)

if __name__ == '__main__':
    unittest.main()