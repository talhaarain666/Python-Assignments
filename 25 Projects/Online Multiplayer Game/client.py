# Client Code (Run this separately)
import pygame
import socket
import pickle

pygame.init()
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
RED, BLUE = (255, 0, 0), (0, 0, 255)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))
player_pos = pickle.loads(client.recv(2048))

running = True
while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_pos = (player_pos[0] - 5, player_pos[1])
    if keys[pygame.K_RIGHT]: player_pos = (player_pos[0] + 5, player_pos[1])
    if keys[pygame.K_UP]: player_pos = (player_pos[0], player_pos[1] - 5)
    if keys[pygame.K_DOWN]: player_pos = (player_pos[0], player_pos[1] + 5)
    client.send(pickle.dumps(player_pos))
    players = pickle.loads(client.recv(2048))
    pygame.draw.rect(screen, RED, (players[0][0], players[0][1], 50, 50))
    pygame.draw.rect(screen, BLUE, (players[1][0], players[1][1], 50, 50))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    clock.tick(30)
pygame.quit()
