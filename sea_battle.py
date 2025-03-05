import socket
import pygame
import threading
from pathlib import Path
import numpy as np
import json

current_dir = Path(__file__).parent

pygame.init()


width, height = 1300, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Морской бой")

ico =  pygame.image.load(str(current_dir / "img" / "ico.ico"))
pygame.display.set_icon(ico)

BLACK = (0, 0, 0)

my_bullets = []
enemy_bulets = []
enemy_map = []

time = 0

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.1.12", 5555))

map_data = client.recv(4096).decode()
player_map = json.loads(map_data)


server_message = ""
turn = False 

TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(TIMER, 1000)

hit_s = pygame.mixer.Sound(str(current_dir / "audio" / "hit.wav"))
miss_s = pygame.mixer.Sound(str(current_dir / "audio" / "miss.wav"))

chanal0 = pygame.mixer.Channel(0)
chanal1 = pygame.mixer.Channel(1)


def listen_to_server():
    global server_message, turn

    while True:
        try:
            data = client.recv(1024).decode('utf-8', 'ignore')
            if data.startswith("Ожидайте"):
                turn = False  
            elif data == "Ваш ход":
                turn = True 
                chanal1.play(miss_s)
            elif data.startswith("Результат"):
                turn = False
                chanal1.play(miss_s)
            elif data.startswith("hit"):
                coords = data.split(":")[1]
                coords = eval(coords)
                enemy_map.append(coords)
                chanal0.play(hit_s)
            elif data.startswith("enemys_udar"):
                coords = data.split(":")[1]
                coords = eval(coords)
                enemy_bulets.append(coords)
                chanal0.play(hit_s)
            else:
                server_message = data
        except Exception as e:
            print(f"Ошибка при получении данных: {e}")
            break

threading.Thread(target=listen_to_server, daemon=True).start()

map = pygame.image.load(str(current_dir / "img" / "map.png"))
sea = pygame.image.load(str(current_dir / "img" / "sea.png"))


def draw_grid():
    w = 100
    h = 100
    for x in range(10):
        for y in range(10):
            if player_map[y][x] == 0:
                pygame.draw.rect(screen, (BLACK), (w, h, 50, 50), 1)
            elif (y,x) in enemy_bulets:
                pygame.draw.rect(screen, (255,0,0), (w, h, 50, 50), 50)
            else:
                pygame.draw.rect(screen, (BLACK), (w, h, 50, 50), 50)
            w += 50
        
        w = 100    
        h += 50
    
def draw_grid2():
    w = 700
    h = 100
    for y in range(10):
        for x in range(10):
            if (x, y) not in my_bullets:
                pygame.draw.rect(screen, (BLACK), (w, h, 50, 50), 1)
            elif (x, y) in enemy_map:
                pygame.draw.rect(screen, (255,0,0), (w, h, 50, 50), 50)
            else:
                pygame.draw.rect(screen, (BLACK), (w, h, 50, 50), 50)
            w += 50
        
        w = 700    
        h += 50

def draw_message():
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(server_message, True, BLACK)
    screen.blit(text, (10, 10))

def send_shot(x, y):
    shot = f"({x},{y})"
    client.send(shot.encode())

run = True
while run:
    screen.blit(map, (0,0))
    screen.blit(sea, (100,100))
    screen.blit(sea, (700,100))
    draw_grid()
    draw_grid2()

    if len(enemy_map) == 20:
        pygame.quit()
        client.close()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and turn:
            mouse_x, mouse_y = event.pos
            if mouse_x >= 700 and mouse_x <= 1200 and mouse_y >= 100 and mouse_y <= 600:
                grid_x = int(np.floor((mouse_x - 700) / 50))
                grid_y = int(np.floor((mouse_y - 100) / 50))
                if (grid_x, grid_y) not in my_bullets:
                    my_bullets.append((grid_x, grid_y))
                    send_shot(grid_x, grid_y)
            
        if event.type == TIMER:
            time += 1
            

    pygame.display.update()

pygame.quit()
client.close()
