import unittest
from float_to_integer import convert_float_to_integer

class TestFloatToInteger(unittest.TestCase):
    def test_positive_float(self):
        self.assertEqual(convert_float_to_integer(3.14), 3)
        
    def test_negative_float(self):
        self.assertEqual(convert_float_to_integer(-3.14), -3)
        
    def test_zero(self):
        self.assertEqual(convert_float_to_integer(0.0), 0)
        
    def test_integer_value_as_float(self):
        self.assertEqual(convert_float_to_integer(5.0), 5)

if __name__ == '__main__':
    unittest.main()