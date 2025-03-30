import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Set screen width and height
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10
SPEED = 15

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling speed
clock = pygame.time.Clock()

# Font for messages
font = pygame.font.SysFont("bahnschrift", 25)

def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])

def display_message(msg, color, y_offset=0):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH // 4, HEIGHT // 3 + y_offset])

def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    snake_list = []
    snake_length = 1

    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            display_message("You Lost! Press C to Play Again or Q to Quit", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, BLOCK_SIZE

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += dx
        y += dy
        screen.fill(BLUE)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            snake_length += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()

# Start the game
game_loop()
