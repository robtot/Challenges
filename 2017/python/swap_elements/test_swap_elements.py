import unittest
from unittest.mock import patch
import tempfile
import os
from swap_elements import swap_elements, get_argv_input_file_lines, parse_swap_elements, SwapError, ParseError

class ParseSwapElementsTestCase(unittest.TestCase):
    """Tests for 'parse_swap_elements' function in 'swap_elements.py'."""
    def test_basic1(self):
        result = parse_swap_elements('1 2 3 4 5 6 7 8 9 : 0-8')
        self.assertEqual(result, '9 2 3 4 5 6 7 8 1')

    def test_basic2(self):
        result = parse_swap_elements('1 2 3 4 5 6 7 8 9 10 : 0-1, 1-3')
        self.assertEqual(result, '2 4 3 1 5 6 7 8 9 10')

    def test_0_and_1_swap(self):
        result = parse_swap_elements('1 2 3 4 : 0-1')
        self.assertEqual(result, '2 1 3 4')

    def test_swap_same(self):
        result = parse_swap_elements('1 2 3 4 : 0-0, 1-1, 2-2, 3-3')
        self.assertEqual(result, '1 2 3 4')

    def test_swap_order(self):
        result = parse_swap_elements('1 2 3 4 : 0-1, 1-2, 2-3')
        self.assertEqual(result, '2 3 4 1')

    def test_long_input(self):
        result = parse_swap_elements('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 : 5-8, 1-3, 9-1, 15-18, 0-1')
        self.assertEqual(result, '10 1 3 2 5 9 7 8 6 4 11 12 13 14 15 19 17 18 16 20')

    def test_multiple_same_nums(self):
        result = parse_swap_elements('1 2 1 4 : 0-1, 1-2, 2-3')
        self.assertEqual(result, '2 1 4 1')

    def test_swap_int_input(self):
        with self.assertRaises(TypeError):
            parse_swap_elements(101)

    def test_mixed_list_types(self):
        result = parse_swap_elements('1 ABC 3 4 : 0-1')
        self.assertEqual(result, 'ABC 1 3 4')

    def test_wrong_format(self):
        with self.assertRaises(ParseError):
            parse_swap_elements('Hello World!')

    def test_wrong_format2(self):
        with self.assertRaises(ParseError):
            parse_swap_elements('1 2 3 4 : xoxo 0-1, 1-2, 2-3')

    def test_wrong_format3(self):
        with self.assertRaises(ParseError):
            parse_swap_elements('1 2 3 4 - 0-1, 1-2, 2-3')

    def test_wrong_format4(self):
        with self.assertRaises(ParseError):
            parse_swap_elements('1 2 3 4 : 0:1, 1:2, 2:3')

    def test_wrong_format5(self):
        with self.assertRaises(ParseError):
            parse_swap_elements('1 2 3 4 : 0-1, 1-x, 2-3')

    def test_empty_string(self):    
        with self.assertRaises(ParseError):
            result = parse_swap_elements('')

    def test_0_and_out_of_bounds_swap(self):
        with self.assertRaises(SwapError):
            parse_swap_elements('1 2 3 4 : 0-10')

    def test_negative_and_3_swap(self):
        #This would ideally raise SwapError due to negative numbers being swapped but ParseError is sufficient
        with self.assertRaises(ParseError):
            parse_swap_elements('1 2 3 4 : -4-3')

class SwapElementsTestCase(unittest.TestCase):
    """Tests for 'swap_elements' function in 'swap_elements.py'."""
    def test_0_and_1_swap(self):
        numbers = [1,2,3,4]
        swap_elements(numbers, 0, 1)
        self.assertEqual(numbers, [2,1,3,4])

    def test_1_and_10_swap(self):
        numbers = [1,2,3,4,5,6,7,8,9,10,11]
        swap_elements(numbers, 1, 10)
        self.assertEqual(numbers, [1,11,3,4,5,6,7,8,9,10,2])

    def test_0_and_out_of_bounds_swap(self):
        numbers = [1,2,3,4]
        with self.assertRaises(SwapError):
            swap_elements(numbers, 0, 10)

    def test_negative_and_3_swap(self):
        numbers = [1,2,3,4]
        with self.assertRaises(SwapError):
            swap_elements(numbers, -4, 3)

    def test_same_number_swap(self):
        numbers = [1,2,3,4]
        swap_elements(numbers, 1, 1)
        self.assertEqual(numbers, [1,2,3,4])

    def test_3_and_0_swap(self):
        numbers = [1,2,3,4]
        swap_elements(numbers, 3, 0)
        self.assertEqual(numbers, [4,2,3,1])

    def test_string_swap(self):
        numbers = [1,2,3,4]
        with self.assertRaises(TypeError):
            swap_elements(numbers, 'yolo', 'habibi')

    def test_string_container_swap(self):
        numbers = [1,2,3,4]
        with self.assertRaises(TypeError):
            swap_elements('numbers', 1, 2)

class GetArgvInputFileLinesTestCase(unittest.TestCase):
    """Tests for 'swap_elements' function in swap_elements.py'."""
    
    @patch('sys.argv', ["testprog"])
    def test_no_argv(self):
        with self.assertRaises(ValueError):
            get_argv_input_file_lines()

    @patch('sys.argv', ["testprog", "testinput.txt"])
    def test_no_file(self):
        with self.assertRaises(FileNotFoundError):
            get_argv_input_file_lines()

    def test_with_file(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'test101\nanother line.\n')
            tf.close()
            with patch('sys.argv', ['testprog', tf.name]):
                lines = get_argv_input_file_lines()
                self.assertIsInstance(lines, list)
                self.assertIsInstance(lines[0], str)
                self.assertIsInstance(lines[1], str)
                self.assertEqual(len(lines), 2)
                self.assertEqual(lines[0], 'test101')
                self.assertEqual(lines[1], 'another line.')
        finally:
            os.remove(tf.name)

if __name__ == '__main__':
    unittest.main()