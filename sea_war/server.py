import socket
from _thread import *
import numpy as np
import random
import json


current_turn = 1 
game_data = {
    "player1": [],
    "player2": [],
}

clients = {}
def find_neighbors(matrix, x, y):
    rows, cols = len(matrix), len(matrix[0]) 
    neighbors = [] 

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1), 
        (-1, -1), (-1, 1), (1, -1), (1, 1) 
    ]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy  
        
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))

    return neighbors

stor = [(0,0),(-1, 0), (1, 0), (0, -1), (0, 1)]

def create_battlefield():
    field = np.zeros((10, 10), dtype=int)

    ships = [
        (4, 1),
        (3, 2),
        (2, 3),
        (1, 4) 
    ]

    def is_valid_position(x, y, length, direction):
        dx, dy = direction
        for i in range(length):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
                return False
            if field[nx][ny] != 0:
                return False

            for dx_check in [-1, 0, 1]:
                for dy_check in [-1, 0, 1]:
                    check_x = nx + dx_check
                    check_y = ny + dy_check
                    if 0 <= check_x < 10 and 0 <= check_y < 10:
                        if field[check_x][check_y] != 0:
                            return False
        return True

    def place_ship(length):
        placed = False
        while not placed:
            x, y = random.randint(0, 9), random.randint(0, 9)
            direction = random.choice([(1, 0), (0, 1)])
            if is_valid_position(x, y, length, direction):
                for i in range(length):
                    field[x + i * direction[0]][y + i * direction[1]] = 1
                placed = True


    for length, count in ships:
        for _ in range(count):
            place_ship(length)

    return field
            

player_1_map = create_battlefield()
player_2_map = create_battlefield()

def send_map_to_client(conn, player_id):
    if player_id == 1:
        player_map = player_1_map.tolist() 
    else:
        player_map = player_2_map.tolist()

    map_data = json.dumps(player_map) 
    conn.sendall(map_data.encode()) 


def handle_client(conn, addr, player_id):
    global current_turn
    print(f"Игрок {player_id} подключился: {addr}")
    
    clients[player_id] = conn
    
    send_map_to_client(conn, player_id)

    try:
        while True:
            if current_turn != player_id:
                continue  

            if current_turn == 1:
                clients[1].send("Ваш ход".encode())
            elif current_turn == 2:
                clients[2].send("Ваш ход".encode())

            data = conn.recv(1024)
            if not data:
                break

            shot = data.decode()
            
            shot = eval(shot)

            print(f"Игрок {player_id} сделал выстрел: {shot}")
            
            
            if current_turn != 1:
                clients[1].send(f"enemys_udar:{shot}".encode())
                if player_1_map[shot[0]][shot[1]] == 1:
                    result = "hit" 
                    conn.send(f"hit:{shot}".encode())
                    current_turn = 2
                else:
                    result = "miss" 
                    conn.send(f"Результат:{result}".encode())
                    current_turn = 1
                    print(f"Ход передан игроку {current_turn}")
            else:
                clients[2].send(f"enemys_udar:{shot}".encode())
                if player_2_map[shot[0]][shot[1]] == 1:
                    result = "hit" 
                    conn.send(f"hit:{shot}".encode())
                    current_turn = 1
                else:
                    result = "miss" 
                    conn.send(f"Результат:{result}".encode())
                    current_turn = 2
                    print(f"Ход передан игроку {current_turn}")
                    
            

    except Exception as e:
        print(f"Ошибка: {e}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.12", 5555))
    server.listen()
    print("Ожидаем подключения игроков...")

    player_id = 1

    while True:
        conn, addr = server.accept()
        start_new_thread(handle_client, (conn, addr ,player_id))
        player_id = 2 if player_id == 1 else 1

if __name__ == "__main__":
    start_server()
