import unittest
from unittest.mock import patch
from io import StringIO
import age

class TestPrintAge(unittest.TestCase):
    @patch('builtins.input', return_value='25')
    def test_read_user_age(self, mock_input):
        result = age.read_user_age()
        self.assertEqual(result, 25)
        mock_input.assert_called_once_with("Enter your age: ")

    @patch('builtins.input', return_value='18')
    def test_read_user_age_18(self, mock_input):
        result = age.read_user_age()
        self.assertEqual(result, 18)

if __name__ == '__main__':
    unittest.main()