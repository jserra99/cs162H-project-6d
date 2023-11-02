# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6d; Row Puzzle Tester

import unittest
from row_puzzle import row_puzzle


class RowPuzzleTester(unittest.TestCase):

    def test_row_puzzle(self):
        """ Test row_puzzle() """
        row_one = [2, 0, 5, 3, 1, 3, 1, 4, 0]
        row_two = [1, 3, 2, 1, 3, 4, 0]
        self.assertTrue(row_puzzle(row_one))
        self.assertFalse(row_puzzle(row_two))
