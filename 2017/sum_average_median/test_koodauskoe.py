"""Unit tests for koodauskoe (sum_mean_median program)"""
import unittest
from unittest.mock import patch
import tempfile
import os
import sys
from contextlib import contextmanager
from io import StringIO
from koodauskoe import get_args, get_lines_from_file, avg, median, get_comparison_result_finnish
from koodauskoe import main as koodauskoe_main

@contextmanager
def captured_output():
    new_out = StringIO()
    old_out= sys.stdout
    try:
        sys.stdout = new_out
        yield sys.stdout
    finally:
        sys.stdout = old_out

class TestGetArgsTestCase(unittest.TestCase):
    @patch('sys.argv', ['testprog'])
    def test_no_args(self):
        with self.assertRaises(IndexError):
            get_args()

    @patch('sys.argv', ['testprog', 'fakefile'])
    def test_1_arg(self):
        with self.assertRaises(IndexError):
            get_args()

    @patch('sys.argv', ['testprog', 'testfile.txt', 'sum', 'gt'])
    def test_missing_2nd_optional_argument(self):
        with self.assertRaises(IndexError):
            get_args()

    @patch('sys.argv', ['testprog', 'fakefile', 'sum'])
    def test_no_optional_args(self):
        result = get_args()
        self.assertEqual(result[0], 'fakefile')
        self.assertEqual(result[1], 'sum')
        self.assertEqual(result[2], None)
        self.assertEqual(result[3], None)

    @patch('sys.argv', ['testprog', 'testfile.txt', 'sum', 'illegalargument', '20'])
    def test_illegal_1st_optional_argument(self):
        with self.assertRaises(ValueError):
            get_args()

    @patch('sys.argv', ['testprog', 'testfile.txt', 'sum', 'lt', 'illegalstringargument'])
    def test_illegal_2nd_optional_argument(self):
        with self.assertRaises(ValueError):
            get_args()

    @patch('sys.argv', ['testprog', 'fakefile', 'sum', 'lt', '50'])
    def test_with_optional_args(self):
        result = get_args()
        self.assertEqual(result[0], 'fakefile')
        self.assertEqual(result[1], 'sum')
        self.assertEqual(result[2], 'lt')
        self.assertEqual(result[3], 50)

    @patch('sys.argv', ['testprog', 'fakefile', 'illegalargument'])
    def test_illegal_2nd_arg(self):
        with self.assertRaises(ValueError):
            get_args()

    @patch('sys.argv', ['testprog', 'sum', 'sum', 'sum', 'sum'])
    def test_all_sum(self):
        with self.assertRaises(ValueError):
            get_args()

    @patch('sys.argv', ['testprog', 'fakefile', 'sum', 'lt', '50', 'redundant', 'redundant'])
    def test_with_redundant_args(self):
        result = get_args()
        self.assertEqual(result[0], 'fakefile')
        self.assertEqual(result[1], 'sum')
        self.assertEqual(result[2], 'lt')
        self.assertEqual(result[3], 50)

class TestGetLinesFromFileTestCase(unittest.TestCase):
    def test_no_file(self):
        with self.assertRaises(FileNotFoundError):
            get_lines_from_file('shouldnotexist1924103.txt')

    def test_with_file(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'line1\nline2\n333\n')
            tf.close()
            lines = get_lines_from_file(tf.name)
            self.assertIsInstance(lines, list)
            self.assertIsInstance(lines[0], str)
            self.assertIsInstance(lines[1], str)
            self.assertIsInstance(lines[2], str)
            self.assertEqual(len(lines), 3)
            self.assertEqual(lines[0], 'line1')
            self.assertEqual(lines[1], 'line2')
            self.assertEqual(lines[2], '333')
        finally:
            os.remove(tf.name)

    def test_with_empty_file(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'')
            tf.close()
            lines = get_lines_from_file(tf.name)
            self.assertIsInstance(lines, list)
            self.assertEqual(len(lines), 0)
        finally:
            os.remove(tf.name)

    def test_with_space(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b' ')
            tf.close()
            lines = get_lines_from_file(tf.name)
            self.assertIsInstance(lines, list)
            self.assertEqual(len(lines), 0)
        finally:
            os.remove(tf.name)

    def test_with_single_char(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'A')
            tf.close()
            lines = get_lines_from_file(tf.name)
            self.assertIsInstance(lines, list)
            self.assertEqual(len(lines), 1)
            self.assertIsInstance(lines[0], str)
            self.assertEqual(lines[0], 'A')
        finally:
            os.remove(tf.name)

    def test_with_empty_lines(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'A\n \nB\n    \nC\n  \n')
            tf.close()
            lines = get_lines_from_file(tf.name)
            print('lines = ' + str(lines))
            self.assertIsInstance(lines, list)
            self.assertEqual(len(lines), 3)
            self.assertIsInstance(lines[0], str)
            self.assertIsInstance(lines[1], str)
            self.assertIsInstance(lines[2], str)
            self.assertEqual(lines[0], 'A')
            self.assertEqual(lines[1], 'B')
            self.assertEqual(lines[2], 'C')
        finally:
            os.remove(tf.name)

    def test_with_redundant_spaces(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'A       \nB   \n  C \n')
            tf.close()
            lines = get_lines_from_file(tf.name)
            print('lines = ' + str(lines))
            self.assertIsInstance(lines, list)
            self.assertEqual(len(lines), 3)
            self.assertIsInstance(lines[0], str)
            self.assertIsInstance(lines[1], str)
            self.assertIsInstance(lines[2], str)
            self.assertEqual(lines[0], 'A')
            self.assertEqual(lines[1], 'B')
            self.assertEqual(lines[2], 'C')
        finally:
            os.remove(tf.name)

    def test_with_integer_argument(self):
        with self.assertRaises(TypeError):
            get_lines_from_file(101)

class TestAvgTestCase(unittest.TestCase):
    def test_with_1_num(self):
        result = avg([5])
        self.assertIsInstance(result, float)
        self.assertEqual(result, 5)

    def test_with_sring_arg(self):
        with self.assertRaises(TypeError):
            avg('hello')

    def test_with_unordered(self):
        result = avg([4, 5, 1, 3, 2])
        self.assertIsInstance(result, float)
        self.assertEqual(3, result)

    def test_with_sring_in_list_arg(self):
        with self.assertRaises(TypeError):
            avg([1, 2, 'hello', 4])

    def test_with_multiple_same_nums(self):
        result = avg([5, 5, 5, 2, 2])
        self.assertIsInstance(result, float)
        self.assertEqual(19/5, result)

    def test_with_multiple_same_nums_floats(self):
        result = avg([5.00, 5.00, 5.00, 2.00, 2.00])
        self.assertIsInstance(result, float)
        self.assertEqual(19/5, result)

class TestMedianTestCase(unittest.TestCase):
    def test_with_1_num(self):
        result = median([5])
        self.assertEqual(result, 5)

    def test_with_sring_arg(self):
        with self.assertRaises(TypeError):
            median('hello')

    def test_with_even_set_of_nums(self):
        result = median([1, 2, 3, 4])
        self.assertEqual((2, 3), result)

    def test_with_odd_set_of_nums(self):
        result = median([1, 2, 3, 4, 5])
        self.assertEqual(3, result)

    def test_with_even_set_of_nums_unordered(self):
        result = median([4, 2, 1, 3])
        self.assertIsInstance(result, tuple)
        self.assertEqual((2, 3), result)

    def test_with_odd_set_of_nums_unordered(self):
        result = median([4, 5, 1, 3, 2])
        self.assertEqual(3, result)

    def test_with_sring_in_list_arg(self):
        with self.assertRaises(TypeError):
            median([1, 2, 'hello', 4])

    def test_with_multiple_same_nums_odd(self):
        result = median([5, 5, 5, 2, 2])
        self.assertEqual(5, result)

    def test_with_multiple_same_nums_odd_floats(self):
        result = median([5.00, 5.00, 5.00, 2.00, 2.00])
        self.assertEqual(5, result)

    def test_with_multiple_same_nums_even(self):
        result = median([5, 5, 5, 2, 2, 2])
        self.assertIsInstance(result, tuple)
        self.assertEqual((2, 5), result)

    def test_with_multiple_same_nums_even_floats(self):
        result = median([5.00, 5.00, 5.00, 2.00, 2.00, 2.00])
        self.assertIsInstance(result, tuple)
        self.assertEqual((2, 5), result)

class TestSumTestCase(unittest.TestCase):
    def test_with_1_num(self):
        result = sum([5])
        self.assertEqual(result, 5)

    def test_with_sring_arg(self):
        with self.assertRaises(TypeError):
            sum('hello')

    def test_with_4_nums(self):
        result = sum([1, 2, 3, 4])
        self.assertEqual(10, result)

    def test_with_4_nums_unordered(self):
        result = sum([4, 2, 1, 3])
        self.assertEqual(10, result)

    def test_with_4_nums_unordered_floats(self):
        result = sum([4.00, 2.00, 1.00, 3.00])
        self.assertEqual(10, result)

    def test_with_sring_in_list_arg(self):
        with self.assertRaises(TypeError):
            sum([1, 2, 'hello', 4])

    def test_with_multiple_same_nums(self):
        result = sum([5, 5, 5, 2, 2])
        self.assertEqual(19, result)

class TestGetComparisonResultFinnish(unittest.TestCase):
    def test_eq_1_1(self):
        result = get_comparison_result_finnish('eq', 1, 1)
        self.assertEqual(result, '1 on yhtä suuri kuin 1')

    def test_eq_1_6(self):
        result = get_comparison_result_finnish('eq', 1, 6)
        self.assertEqual(result, '1 ei ole yhtä suuri kuin 6')

    def test_eq_157_12(self):
        result = get_comparison_result_finnish('eq', 157, 12)
        self.assertEqual(result, '157 ei ole yhtä suuri kuin 12')

    def test_eq_1_1_float(self):
        result = get_comparison_result_finnish('eq', 1.00, 1.00)
        self.assertEqual(result, '1.0 on yhtä suuri kuin 1.0')

    def test_eq_1_6_float(self):
        result = get_comparison_result_finnish('eq', 1.00, 6.00)
        self.assertEqual(result, '1.0 ei ole yhtä suuri kuin 6.0')

    def test_eq_157_12_float(self):
        result = get_comparison_result_finnish('eq', 157.00, 12.00)
        self.assertEqual(result, '157.0 ei ole yhtä suuri kuin 12.0')

    def test_lt_1_1d1_float(self):
        result = get_comparison_result_finnish('lt', 1, 1.1)
        self.assertEqual(result, '1 on pienempi kuin 1.1')

    def test_gt_1_1(self):
        result = get_comparison_result_finnish('gt', 1, 1)
        self.assertEqual(result, '1 ei ole suurempi kuin 1')

    def test_gt_1_6(self):
        result = get_comparison_result_finnish('gt', 1, 6)
        self.assertEqual(result, '1 ei ole suurempi kuin 6')

    def test_gt_157_12(self):
        result = get_comparison_result_finnish('gt', 157, 12)
        self.assertEqual(result, '157 on suurempi kuin 12')

    def test_lt_1_1(self):
        result = get_comparison_result_finnish('lt', 1, 1)
        self.assertEqual(result, '1 ei ole pienempi kuin 1')

    def test_lt_1_6(self):
        result = get_comparison_result_finnish('lt', 1, 6)
        self.assertEqual(result, '1 on pienempi kuin 6')

    def test_lt_157_12(self):
        result = get_comparison_result_finnish('lt', 157, 12)
        self.assertEqual(result, '157 ei ole pienempi kuin 12')

class TestMainTestCase(unittest.TestCase):
    @patch('sys.argv', ['testprog'])
    def test_no_args(self):
        with self.assertRaises(IndexError):
            koodauskoe_main()

    @patch('sys.argv', ['testprog', 'fakefile'])
    def test_1_arg(self):
        with self.assertRaises(IndexError):
            koodauskoe_main()

    @patch('sys.argv', ['testprog', 'testfile.txt', 'sum', 'gt'])
    def test_missing_2nd_optional_argument(self):
        with self.assertRaises(IndexError):
            koodauskoe_main()

    @patch('sys.argv', ['testprog', 'testfile.txt', 'sum', 'illegalargument', '20'])
    def test_illegal_1st_optional_argument(self):
        with self.assertRaises(ValueError):
            koodauskoe_main()

    @patch('sys.argv', ['testprog', 'testfile.txt', 'sum', 'lt', 'illegalstringargument'])
    def test_illegal_2nd_optional_argument(self):
        with self.assertRaises(ValueError):
            koodauskoe_main()

    @patch('sys.argv', ['testprog', 'fakefile', 'illegalargument'])
    def test_illegal_2nd_arg(self):
        with self.assertRaises(ValueError):
            koodauskoe_main()

    @patch('sys.argv', ['testprog', 'sum', 'sum', 'sum', 'sum'])
    def test_all_sum(self):
        with self.assertRaises(ValueError):
            koodauskoe_main()

    def test_with_string_value_in_file(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'5\nX\n3\n')
            tf.close()
            with patch('sys.argv', ['testprog', tf.name, 'sum', 'lt', '50']):
                with self.assertRaises(ValueError):
                    koodauskoe_main()

        finally:
            os.remove(tf.name)

    def test_case1(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'4\n2\n1\n3\n')
            tf.close()
            with patch('sys.argv', ['testprog', tf.name, 'sum', 'lt', '50']):
                with captured_output() as out:
                    koodauskoe_main()
                    output = out.getvalue().strip()
                    self.assertEqual(output, 'Summa on: 10\n10 on pienempi kuin 50')

        finally:
            os.remove(tf.name)

    def test_case2(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'4\n2\n1\n3\n')
            tf.close()
            with patch('sys.argv', ['testprog', tf.name, 'avg', 'eq', '2.5']):
                with captured_output() as out:
                    koodauskoe_main()
                    output = out.getvalue().strip()
                    self.assertEqual(output, 'Keskiarvo on: 2.5\n2.5 on yhtä suuri kuin 2.5')

        finally:
            os.remove(tf.name)

    def test_case3(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'4\n2\n1\n3\n')
            tf.close()
            with patch('sys.argv', ['testprog', tf.name, 'median', 'gt', '2']):
                with captured_output() as out:
                    koodauskoe_main()
                    output = out.getvalue().strip()
                    self.assertEqual(output, 'Mediaani on: 2 ja 3\n2 ei ole suurempi kuin 2\n3 on suurempi kuin 2')

        finally:
            os.remove(tf.name)

    def test_float_in_file(self):
        try:
            tf = tempfile.NamedTemporaryFile(dir='.', delete=False)
            tf.write(b'4\n2\n1.0\n3\n')
            tf.close()
            with patch('sys.argv', ['testprog', tf.name, 'median', 'gt', '2']):
                with self.assertRaises(ValueError):
                    koodauskoe_main()
                    
        finally:
            os.remove(tf.name)

if __name__ == '__main__':
    unittest.main()