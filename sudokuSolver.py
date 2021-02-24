import numpy as np

def isPossible(y,x,n):
    global SudokuMatrix
    for i in range(0, 9):
        if SudokuMatrix[y][i] == n:
            return False
    for i in range(0, 9):
        if SudokuMatrix[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range (0, 3):
        for j in range(0,3):
            if SudokuMatrix[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global SudokuMatrix
    for y in range(9):
        for x in range(9):
            if SudokuMatrix[y][x] == 0:
                for n in range(1,10):
                    if isPossible(y,x,n):
                        SudokuMatrix[y][x] = n
                        solve()
                        SudokuMatrix[y][x] = 0
                return
    print(np.matrix(SudokuMatrix))


SudokuMatrix = [[9, 0, 0, 0, 8, 0, 3, 0, 0],
                [0, 0, 0, 2, 5, 0, 7, 0, 0],
                [0, 2, 0, 3, 0, 0, 0, 0, 4],
                [0, 9, 4, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 7, 3, 0, 5, 6, 0],
                [7, 0, 5, 0, 6, 0, 4, 0, 0],
                [0, 0, 7, 8, 0, 3, 9, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 3],
                [3, 0, 0, 0, 0, 0, 0, 0, 2]]

print("\n")
print(np.matrix(SudokuMatrix))

solve()