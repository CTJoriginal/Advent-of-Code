import unittest
from Day_4 import *
import numpy as np

class Day4(unittest.TestCase):

    def test_direction(self):
        self.assertEqual(Part1("2024\\4\\DirectionTest.txt"), 8)
    
    def test_Puzzle_Small_Input(self):
        self.assertEqual(Part1("2024\\4\\TestInput.txt"), 18)
    


if __name__ == '__main__':
    unittest.main()