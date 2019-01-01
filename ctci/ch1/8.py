import pytest

def zeroify(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    row = len(matrix) * [False]
    col = len(matrix[0]) * [False]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                print(row,col)
                row[i] = True
                col[j] = True
    for i in range(len(matrix[0])):
        if col[i] == True:
            for j in range(len(matrix)):
               matrix[j][i] = 0
    for j in range(len(matrix)):
        if row[j] == True:
            for i in range(len(matrix[0])):
                matrix[j][i] = 0
    return matrix

def test1():
    assert zeroify([[0, 1]]) == [[0,0]]
def test2():
    assert zeroify([[0, 1, 0],
                    [1, 1, 1],
                    [0, 1, 0]]) == [[0, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 0]]
