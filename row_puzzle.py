# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6d; Row Puzzle

def row_puzzle(row: list[int], index=0):
    """ Returns true if the puzzle is solvable. """
    if index == len(row) - 1:
        return True
    if index >= len(row) or row[index] == 0:
        return False
    shift = row[index]
    row[index] = 0
    if row_puzzle(row, index + shift) or row_puzzle(row, index - shift):
        row[index] = shift
        return True
    row[index] = shift
    return False
