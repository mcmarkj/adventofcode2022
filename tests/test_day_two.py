import unittest
from days.two import play_rock, play_paper, play_scissors, determine_winner, get_desired_result, split_plays


class TestDayOne(unittest.TestCase):
    def test_splits_plays_correctly(self):
        input = ["x z", "o l"]
        result = split_plays(input)
        self.assertEqual(result, [["x", "z"], ["o", "l"]])

    def test_rock_should_win_against_scissors(self):
        result = play_rock("scissors")
        self.assertTrue(result)

        result = determine_winner("rock", "scissors")
        self.assertEqual(result, 1)

    def test_rock_should_loose_against_paper(self):
        result = play_rock("paper")
        self.assertFalse(result)

        result = determine_winner("rock", "paper")
        self.assertEqual(result, 2)

    def test_paper_should_win_against_rock(self):
        result = play_paper("rock")
        self.assertTrue(result)

        result = determine_winner("paper", "rock")
        self.assertEqual(result, 1)

    def test_paper_should_lose_against_scissors(self):
        result = play_paper("scissors")
        self.assertFalse(result)

        result = determine_winner("paper", "scissors")
        self.assertEqual(result, 2)

    def test_scissors_should_win_against_paper(self):
        result = play_scissors("paper")
        self.assertTrue(result)

        result = determine_winner("scissors", "paper")
        self.assertEqual(result, 1)

    def test_scissors_should_lose_against_rock(self):
        result = play_scissors("rock")
        self.assertFalse(result)

        result = determine_winner("scissors", "rock")
        self.assertEqual(result, 2)

    def test_translates_actual_moves_to_a_losing_game(self):
        # A = Rock, B = Paper, C = Scissors
        # X = Lose, Y = Draw, Z = Win
        losing_game = [["A", "X"]]
        result = get_desired_result(losing_game)
        self.assertEqual(result, [["rock", "scissors"]])

    def test_translates_actual_moves_to_a_winning_game(self):
        # A = Rock, B = Paper, C = Scissors
        # X = Lose, Y = Draw, Z = Win
        losing_game = [["B", "Z"]]
        result = get_desired_result(losing_game)
        self.assertEqual(result, [["paper", "scissors"]])

    def test_translates_actual_moves_to_a_draw_game(self):
        # A = Rock, B = Paper, C = Scissors
        # X = Lose, Y = Draw, Z = Win
        losing_game = [["B", "Y"]]
        result = get_desired_result(losing_game)
        self.assertEqual(result, [["paper", "paper"]])
