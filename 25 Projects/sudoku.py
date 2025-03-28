def find_empty_location(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None

def is_valid(puzzle, row, col, guess):
    # Check row
    if guess in puzzle[row]:
        return False
    
    # Check column
    if guess in [puzzle[r][col] for r in range(9)]:
        return False
    
    # Check 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for r in range(box_row_start, box_row_start + 3):
        for c in range(box_col_start, box_col_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):
    empty_location = find_empty_location(puzzle)
    
    if empty_location is None:
        return True  # Solved
    
    row, col = empty_location

    for guess in range(1, 10):
        if is_valid(puzzle, row, col, guess):
            puzzle[row][col] = guess
            
            if solve_sudoku(puzzle):
                return True

            puzzle[row][col] = -1  # Undo and try next number

    return False


if __name__ == "__main__":
    # Example Sudoku puzzle with -1 representing empty cells
    example_board = [
        [5, 3, -1, -1, 7, -1, -1, -1, -1],
        [6, -1, -1, 1, 9, 5, -1, -1, -1],
        [-1, 9, 8, -1, -1, -1, -1, 6, -1],
        [8, -1, -1, -1, 6, -1, -1, -1, 3],
        [4, -1, -1, 8, -1, 3, -1, -1, 1],
        [7, -1, -1, -1, 2, -1, -1, -1, 6],
        [-1, 6, -1, -1, -1, -1, 2, 8, -1],
        [-1, -1, -1, 4, 1, 9, -1, -1, 5],
        [-1, -1, -1, -1, 8, -1, -1, 7, 9]  # Fixed: Proper 9-element row
    ]

    # print(solve_sudoku(example_board))
    # print(example_board)

    if solve_sudoku(example_board):
        for row in example_board:
            print(row)
    else:
        print("No solution exists")