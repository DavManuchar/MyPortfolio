from concurrent.futures import ThreadPoolExecutor
import pygame
import math
from pathlib import Path

current_dir = Path(__file__).parent

pygame.init()

width = 1800
height = 1000
org_size = 20
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("micro world")

ico =  pygame.image.load(str(current_dir /  "ico.ico"))
pygame.display.set_icon(ico)

matrix = [[(x, y) for x in range(0, width, org_size)] for y in range(0, height, org_size)]
organic = []

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


def update_cell(matrix, organic, i, j):
    neighbors = find_neighbors(matrix, i, j)
    count = 0

    for z in range(len(neighbors)):
        if matrix[neighbors[z][0]][neighbors[z][1]] in organic:
            count += 1


    if count == 3 and matrix[i][j] not in organic: # cnvuma te che
        return ("add", matrix[i][j])
    elif (count < 2 or count > 3) and matrix[i][j] in organic: #mernuma te che
        return ("remove", matrix[i][j])
    return None


def process_matrix(matrix, organic):
    changes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result = update_cell(matrix, organic, i, j)
            if result:
                changes.append(result)
    return changes


START_PROCESS = pygame.USEREVENT + 1
pygame.time.set_timer(START_PROCESS, 1000)


executor = ThreadPoolExecutor(max_workers=4)

start = False
running = True
future = None

while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if start == True:
                  start = False
                else:
                  start = True
                  pygame.time.set_timer(START_PROCESS, 500)

        if event.type == START_PROCESS and future is None and start == True:
            future = executor.submit(process_matrix, matrix, organic)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            y, x = math.floor(x / org_size), math.floor(y / org_size)
            if matrix[x][y] not in organic:
                organic.append(matrix[x][y])

    if future and future.done():
        changes = future.result()
        for action, cell in changes:
            if action == "add" and cell not in organic:
                organic.append(cell)
            elif action == "remove" and cell in organic:
                organic.remove(cell)
        future = None


    for y in range(0, height, org_size):
        for x in range(0, width, org_size):
            if (x, y) in organic:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, org_size, org_size), 0)
            else:
                pygame.draw.rect(screen, (166, 166, 166), (x, y, org_size, org_size), 1)

    pygame.display.flip() 

executor.shutdown(wait=True)
pygame.quit()
