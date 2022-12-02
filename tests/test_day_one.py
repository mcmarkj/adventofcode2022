import unittest
from days.one import sort_by_heaviest, split_to_elves


class TestDayOne(unittest.TestCase):
    def test_sorting_by_heaviest_is_correct(self):
        set_of_numbers = [[1, 74, 22], [94, 0, 1], [1000, 43, 2], [-1, 0]]
        response = sort_by_heaviest(set_of_numbers)
        self.assertEqual(response, [[1000, 43, 2], [1, 74, 22], [94, 0, 1], [-1, 0]])

    def test_splitting_returns_correct_number_of_elves(self):
        input_elves = ["43", "43", "43", "43", "", "27", "", "43", "43"]
        response = split_to_elves(input_elves)
        self.assertEqual(len(response), 3)
