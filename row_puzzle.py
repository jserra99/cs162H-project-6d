# Author: Joseph Serra
# GitHub username: jserra99
# Date: 11/2/2023
# Description: Project-6d; Row Puzzle


def row_puzzle(row: list[int], index=0, memo=None):
    """
    Returns true if the puzzle is solvable.
    """
    if memo is None:
        memo = {}
    if index in memo:
        return memo[index]
    if index == len(row) - 1:
        memo[index] = True
        return True
    if index < 0 or index >= len(row) or row[index] == 0:
        memo[index] = False
        return False
    shift = row[index]
    row[index] = 0
    right = index + shift < len(row) and row_puzzle(row, index + shift, memo)
    left = index - shift >= 0 and row_puzzle(row, index - shift, memo)
    row[index] = shift
    memo[index] = right or left
    return memo[index]
