from typing import List
import random

class Solution:

    @staticmethod
    def generate_board(num_cells: int = 17) -> List[List[str]]:
        board = [['.' for _ in range(9)] for _ in range(9)]
        # Solve an empty board to generate a random valid board
        Solution.solve_sudoku(board)
        # Ensure number of cells is valid
        num = num_cells if num_cells >= 17 else 17
        num = num if num <= 80 else 80
        count = 81
        # Remove cells until the number of cells is equal to num
        while count > num:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] != '.':
                board[row][col] = '.'
                count -= 1
        return board

    @staticmethod
    def solve_sudoku(board: List[List[str]]) -> None:
        Solution.__solve_helper(board, 0, 0)
    
    # Recursive helper method to solve the sudoku
    def __solve_helper(board: List[List[str]], row: int, col: int) -> bool:
        if board[row][col] != '.':
            if col < 8:
                return Solution.__solve_helper(board, row, col + 1)
            elif row < 8:
                return Solution.__solve_helper(board, row + 1, 0)
            else:
                return Solution.__is_valid(board)
        
        for val in Solution.__get_possible_vals(board, row, col):
            board[row][col] = val
            result = False
            if col < 8:
                result = Solution.__solve_helper(board, row, col + 1)
            elif row < 8:
                result = Solution.__solve_helper(board, row + 1, 0)
            else:
                result = Solution.__is_valid(board)
            if result:
                return True
        board[row][col] = '.'
        return False

    # Returns a list of possible values for the given cell           
    def __get_possible_vals(board: List[List[str]], row: int, col: int) -> List[str]:
        rowVals = [val for val in board[row] if val != '.']
        colVals = [board[k][col] for k in range(9) if board[k][col] != '.']
        # Square
        squareVals = []
        startRow = int(row/3)*3
        endRow = startRow + 3
        startCol = int(col/3)*3
        endCol = startCol + 3
        for i in range(startRow, endRow):
            for j in range(startCol, endCol):
                squareVals.append(board[i][j])
        return list(set(map(lambda x : str(x), range(1, 10))) - (set(rowVals) | set(colVals) | set(squareVals)))
        
    # Returns true if the board is valid, false otherwise
    def __is_valid(board: List[List[str]]) -> bool:
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if val == '.':
                    continue
                # Check row
                elif val in row[:j]:
                    return False
                # Check column
                elif val in [board[k][j] for k in range(i)]:
                    return False
        # Check squares
        for i in range(3):
            rows = board[i*3:i*3+3]
            for j in range(3):
                squareRows = [rows[k][j*3:j*3+3] for k in range(3)]
                square = squareRows[0] + squareRows[1] + squareRows[2]
                for k, val in enumerate(square):
                    if val == '.':
                        continue
                    # Check row
                    elif val in square[:k]:
                        return False
        return True

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
# Generate a board with 17 cells filled
board = Solution.generate_board()
print('Initial board:')
for row in board:
    print(*row)
Solution.solve_sudoku(board)
print('Solved board:')
for row in board:
    print(*row)