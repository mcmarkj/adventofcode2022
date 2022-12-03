import unittest
from days.three import split_compartments, get_priority


class TestDayThree(unittest.TestCase):
    def test_splits_compartments_correctly(self):
        input = "abcdefghijkl"
        result = split_compartments(input)
        self.assertEqual(result, ["abcdef", "ghijkl"])

        input = "abcdefghijklm"
        result = split_compartments(input)
        self.assertEqual(result, ["abcdefg", "hijklm"])

    def test_subtraction_returns_correct_number(self):
        input = "A"
        self.assertEqual(get_priority(input), 27)

        input = "a"
        self.assertEqual(get_priority(input), 1)

        input = "Z"
        self.assertEqual(get_priority(input), 52)

        input = "z"
        self.assertEqual(get_priority(input), 26)
