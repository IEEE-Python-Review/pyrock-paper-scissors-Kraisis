import unittest
from pyRockPaperScissors import *
from unittest.mock import patch


class TestRockPaperScissors(unittest.TestCase):

    @staticmethod
    def test_Computer():
        play = Computer()
        assert play == "rock" or play == "paper" or play == "scissors"

    @patch('pyRockPaperScissors.play', return_value='1')
    def test_rock(self, input):
        self.assertEqual(Human(), 'rock')

    @patch('pyRockPaperScissors.play', return_value='2')
    def test_paper(self, input):
        self.assertEqual(Human(), 'paper')

    @patch('pyRockPaperScissors.play', return_value='3')
    def test_scissors(self, input):
        self.assertEqual(Human(), 'scissors')

    @patch('pyRockPaperScissors.play', return_value='4')
    def test_invalid_play(self, input):
        self.assertEqual(Human(), 'Invalid Play')


if __name__ == "__main__":
    unittest.main()
