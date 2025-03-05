from pathlib import Path
import pygame
import time


current_dir = Path(__file__).parent



pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Pairs")

player1 = [0, 100, 10, 150]
player2 = [790, 100, 800, 150]

p1 = 0
p2 = 0

ball = [400, 300, 10] 
ball_speed = [0.1, 0.1]

log_font = pygame.font.Font(None, 150) 

START_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(START_TIMER, 1000)

running = True
while running:
  screen.fill((0,0,0))

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

      if event.type == START_TIMER:
        if ball_speed[0] > 0:
          ball_speed[0] += 0.01
        elif ball_speed[0] < 0:
          ball_speed[0] -= 0.01
        if ball_speed[1] > 0:
          ball_speed[1] += 0.01
        elif ball_speed[1] < 0:
          ball_speed[1] -= 0.01


  keys = pygame.key.get_pressed()

  if keys[pygame.K_w] and player1[1] >= 0:
      player1[1] -= 1
  if keys[pygame.K_s] and player1[1] + 150 < 500:
      player1[1] += 0.5
    
  if keys[pygame.K_UP] and player2[1] >= 0:
      player2[1] -= 1
  if keys[pygame.K_DOWN] and player2[1] + 150 < 500:
      player2[1] += 0.5

  ball[0] += ball_speed[0]
  ball[1] += ball_speed[1] 

  if (player1[0] < ball[0] < player1[0] + player1[2] and
    player1[1] < ball[1] < player1[1] + player1[3]):
    ball_speed[0] = -ball_speed[0]
    ball_speed[1] = +ball_speed[1]

  elif (player2[0] < ball[0] < player2[0] + player2[2] and
    player2[1] < ball[1] < player2[1] + player2[3]):
    ball_speed[0] = -ball_speed[0]
    ball_speed[1] = +ball_speed[1]

  elif ball[0] < 0:
    p2 += 1
    ball = [400, 300, 10] 
    ball_speed = [0.1, 0.1]
    time.sleep(1)
  elif ball[0] > 800:
    p1 += 1
    ball = [400, 300, 10] 
    ball_speed = [0.1, 0.1]
    time.sleep(1) 


  
  if ball[1] <= 0 or ball[1] >= 500:
    ball_speed[1] = -ball_speed[1]

  x1 = log_font.render(f'{p1}', True, (200,0,0))
  screen.blit(x1, (100, 200))

  x2 = log_font.render(f'{p2}', True, (0,0,200))
  screen.blit(x2, (650, 200))

  pygame.draw.rect(screen, (200, 200, 200), (395, 0, 5, 500))
  pygame.draw.circle(screen, (200, 200, 200), (397, 240), 100, 5)

  pygame.draw.rect(screen, (200, 0, 0), (player1[0], player1[1], player1[2], player1[3]))
  pygame.draw.rect(screen, (0, 0, 200), (player2[0], player2[1], player2[2], player2[3]))
  pygame.draw.circle(screen, (255, 255, 255), (ball[0], ball[1]), ball[2])


  pygame.display.flip()

pygame.quit() 
