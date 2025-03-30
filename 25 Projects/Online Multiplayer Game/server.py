import socket
import threading
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))  # Change port if needed
server.listen(2)
print("Waiting for connections...")

players = [(100, 100), (400, 100)]  # Player positions

def handle_client(conn, player_id):
    global players
    conn.send(pickle.dumps(players[player_id]))
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            if not data:
                break
            players[player_id] = data  # Update player position
            conn.sendall(pickle.dumps(players))
        except:
            break
    conn.close()

player_id = 0
while player_id < 2:
    conn, addr = server.accept()
    print(f"Player {player_id} connected from {addr}")
    threading.Thread(target=handle_client, args=(conn, player_id)).start()
    player_id += 1
