import numpy as np

def create_board():
    return np.zeros((6, 7), dtype=int)

def print_board(board):
    print(np.flip(board, 0))

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(6):
        if board[r][col] == 0:
            return r

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def winning_move(board, piece):
    # Check horizontal locations
    for c in range(4):
        for r in range(6):
            if (board[r][c] == piece and board[r][c+1] == piece and 
                board[r][c+2] == piece and board[r][c+3] == piece):
                return True
    
    # Check vertical locations
    for c in range(7):
        for r in range(3):
            if (board[r][c] == piece and board[r+1][c] == piece and 
                board[r+2][c] == piece and board[r+3][c] == piece):
                return True
    
    # Check positively sloped diagonals
    for c in range(4):
        for r in range(3):
            if (board[r][c] == piece and board[r+1][c+1] == piece and 
                board[r+2][c+2] == piece and board[r+3][c+3] == piece):
                return True
    
    # Check negatively sloped diagonals
    for c in range(4):
        for r in range(3, 6):
            if (board[r][c] == piece and board[r-1][c+1] == piece and 
                board[r-2][c+2] == piece and board[r-3][c+3] == piece):
                return True
    
    return False

def play_game():
    board = create_board()
    game_over = False
    turn = 0
    
    while not game_over:
        print_board(board)
        col = int(input(f"Player {turn+1}, select a column (0-6): "))
        
        if 0 <= col <= 6 and is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, turn + 1)
            
            if winning_move(board, turn + 1):
                print_board(board)
                print(f"PLAYER {turn+1} WINS!")
                game_over = True
            
            turn = (turn + 1) % 2  # Switch player
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
