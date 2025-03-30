import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLUMNS, ROWS = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
CYAN = (0, 200, 200)
MAGENTA = (200, 0, 200)
YELLOW = (200, 200, 0)
ORANGE = (255, 165, 0)

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
]
SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

class Tetromino:
    def __init__(self, shape):
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPES.index(shape)]
        self.x, self.y = COLUMNS // 2 - len(shape[0]) // 2, 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_grid():
    return [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]

def draw_grid(surface, grid):
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(surface, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_tetromino(surface, tetromino):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(surface, tetromino.color, 
                                 ((tetromino.x + x) * BLOCK_SIZE, (tetromino.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def valid_position(tetromino, grid):
    for y, row in enumerate(tetromino.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x, new_y = tetromino.x + x, tetromino.y + y
                if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or (new_y >= 0 and grid[new_y][new_x] != BLACK):
                    return False
    return True

def clear_lines(grid):
    full_rows = [y for y, row in enumerate(grid) if all(color != BLACK for color in row)]
    for y in full_rows:
        del grid[y]
        grid.insert(0, [BLACK] * COLUMNS)
    return len(full_rows)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    grid = create_grid()
    current_tetromino = Tetromino(random.choice(SHAPES))
    fall_time, fall_speed = 0, 500
    score = 0
    running = True

    while running:
        screen.fill(BLACK)
        draw_grid(screen, grid)
        draw_tetromino(screen, current_tetromino)
        pygame.display.flip()
        
        fall_time += clock.get_rawtime()
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_tetromino.x -= 1
                    if not valid_position(current_tetromino, grid):
                        current_tetromino.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_tetromino.x += 1
                    if not valid_position(current_tetromino, grid):
                        current_tetromino.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_tetromino.y += 1
                    if not valid_position(current_tetromino, grid):
                        current_tetromino.y -= 1
                elif event.key == pygame.K_UP:
                    current_tetromino.rotate()
                    if not valid_position(current_tetromino, grid):
                        current_tetromino.rotate()  # Undo rotation
        
        if fall_time >= fall_speed:
            current_tetromino.y += 1
            if not valid_position(current_tetromino, grid):
                current_tetromino.y -= 1
                for y, row in enumerate(current_tetromino.shape):
                    for x, cell in enumerate(row):
                        if cell:
                            grid[current_tetromino.y + y][current_tetromino.x + x] = current_tetromino.color
                score += clear_lines(grid)
                current_tetromino = Tetromino(random.choice(SHAPES))
                if not valid_position(current_tetromino, grid):
                    print("Game Over! Final Score:", score)
                    running = False
            fall_time = 0
    pygame.quit()

if __name__ == "__main__":
    main()