import random

def create_board(size, mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mine_positions = set()
    
    while len(mine_positions) < mines:
        row, col = random.randint(0, size - 1), random.randint(0, size - 1)
        mine_positions.add((row, col))
    
    for row, col in mine_positions:
        board[row][col] = 'M'
    
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'M':
                continue
            mines_count = sum(
                (nr, nc) in mine_positions
                for nr in range(r - 1, r + 2)
                for nc in range(c - 1, c + 2)
                if 0 <= nr < size and 0 <= nc < size
            )
            board[r][c] = str(mines_count) if mines_count > 0 else ' '
    
    return board, mine_positions

def display_board(board, revealed):
    size = len(board)
    print("   " + " ".join(str(i) for i in range(size)))
    print("  " + "--" * size)
    for r in range(size):
        row_display = [board[r][c] if revealed[r][c] else '#' for c in range(size)]
        print(f"{r} | " + " ".join(row_display))

def play_minesweeper(size=5, mines=5):
    board, mine_positions = create_board(size, mines)
    revealed = [[False] * size for _ in range(size)]
    
    while True:
        display_board(board, revealed)
        try:
            r, c = map(int, input("Enter row and column (e.g., 1 2): ").split())
            if (r, c) in mine_positions:
                print("Game Over! You hit a mine.")
                break
            revealed[r][c] = True
            
            if all(revealed[r][c] or (r, c) in mine_positions for r in range(size) for c in range(size)):
                print("Congratulations! You win!")
                break
        except (ValueError, IndexError):
            print("Invalid input. Try again.")
    
    print("Final board:")
    display_board(board, [[True] * size for _ in range(size)])

if __name__ == "__main__":
    play_minesweeper()