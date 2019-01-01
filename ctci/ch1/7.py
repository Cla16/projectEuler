import pytest

def rotate(matrix):
    """
    The original question says 4 bytes, but were just going to use ints
    The process is nearly identical for bytes, minus some type changes
    """
    if len(matrix) == 0 or len(matrix[0]) != len(matrix):
        return False
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1
        for i in range(first, last):
           offset = i - first
           # save the top
           top = matrix[first][i]
           # left to top
           matrix[first][i] = matrix[last-offset][first]
           # bottom to left
           matrix[last-offset][first] = matrix[last][last-offset]
           # right to bottom
           matrix[last][last-offset] = matrix[i][last]
           # top to right
           matrix[i][last] = top
    return matrix

def testbad_matrix():
    assert rotate([[1, 2, 3],
                   [4, 5, 6]]) == False
def test_invalid_input():
    assert rotate([[]]) == False
def test1():
    assert rotate([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]) == [[7, 4, 1],
                                   [8, 5, 2],
                                   [9, 6, 3]]

