from pathlib import Path
import pygame
import math
import random

current_dir = Path(__file__).parent

pygame.init()
pygame.mixer.init()


width, height = 800, 800

screen = pygame.display.set_mode((width,height))

MAP_WIDTH, MAP_HEIGHT = 4000, 4000
map = pygame.image.load(str(current_dir / "img" / "map1.jpg"))

cars = ["car1", "car2", "car3", "car4", "car5", "car6"]

car = pygame.image.load(str(current_dir / "img" / "cars" / "car1.png"))
img_x, img_y = car.get_size()

car = pygame.transform.scale(car, (img_x, img_y))

rule = pygame.image.load(str(current_dir / "img" / "rule.png"))
rule = pygame.transform.scale(rule, (200, 200))

# r = pygame.image.load(str(current_dir / "img" / "r.png"))
# d = pygame.image.load(str(current_dir / "img" / "d.png"))
# go_to = 0

x, y = 1460, 835
angle = 0 
speed = 4
down = 0
turn = 0

right_left = 0

bots = []

class Bot:
  def __init__(self, img, cord, direction):
    self.img = img
    self.cord = cord
    self.direction = direction
    
  def travel(self):
    self.cord[1] -= 3
    
  def travel_down(self):
    self.cord[1] += 3
    
BOT_TIMER = pygame.USEREVENT + 1

pygame.time.set_timer(BOT_TIMER, 2000)

run = True
while run == True:
  pygame.time.delay(10) 

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
        
    if event.type == BOT_TIMER:
      bots.append(Bot(random.choice(cars), [300, 800], 0))
      bots.append(Bot(random.choice(cars), [160, 0], 1))
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        speed = 0
        
      if event.key == pygame.K_DOWN:
        down = 0
        
                        
  keys = pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]:
    right_left = 1 if keys[pygame.K_RIGHT] else 2
    if keys[pygame.K_LEFT]:
      turn += 0.05
      turn = min(turn, 1.5)
    if keys[pygame.K_RIGHT]:
      turn -= 0.05
      turn = max(turn, -1.5)
  if keys[pygame.K_UP] and y > 0 and y < MAP_HEIGHT and x < MAP_WIDTH: 
    if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
      if right_left == 1:
        turn += 0.05
        turn = min(turn, 0)
      elif right_left == 2:
        turn -= 0.05
        turn = max(turn, 0)
      
    speed += 0.05
    speed = min(speed, 4)
    rad = math.radians(angle)  
    if x >= 0:
      if angle == 270:
        x -= speed * math.sin(rad)
        angle += turn
      elif angle == 180:
        y -= speed * math.cos(rad)
        angle += turn
      elif angle == 90:
        x -= speed * math.sin(rad)
        angle += turn
      elif angle == 0:
        y -= speed * math.cos(rad)
        angle += turn
      else:
        x -= speed * math.sin(rad)
        y -= speed * math.cos(rad)
        angle += turn
      if keys[pygame.K_LEFT]:  
          angle += turn
          if angle > 360:
            angle = 0
      if keys[pygame.K_RIGHT]:
          angle += turn
          if angle < 0:
            angle = 360
      # print(x, y)
  if keys[pygame.K_DOWN] and y > 0 and y < MAP_HEIGHT and x < MAP_WIDTH :
    if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
      if right_left == 1:
        turn += 0.1
        turn = min(turn, 0)
      elif right_left == 2:
        turn -= 0.1
        turn = max(turn, 0)
      
    down += 0.05
    down = min(down, 2)
    rad = math.radians(angle)  
    if angle == 270:
      x += down * math.sin(rad)
      angle -= turn
    elif angle == 180:
      y += down * math.cos(rad)
      angle -= turn
    elif angle == 90:
      x += down * math.sin(rad)
      angle -= turn
    elif angle == 0:
      y += down * math.cos(rad)
      angle -= turn
    else:
      x += down * math.sin(rad)
      y += down * math.cos(rad)
      angle -= turn
    if keys[pygame.K_LEFT] :  
      angle -= turn
      if angle < 0:
          angle = 360
    if keys[pygame.K_RIGHT] :
        angle -= turn
        if angle > 360:
          angle = 0
            
  
  if x > 400 and x < MAP_WIDTH - 400:    
    offset_x = x - width // 2
  if y > 400 and y < MAP_HEIGHT - 400 :
    offset_y = y - height // 2

  screen.blit(map, (-offset_x, -offset_y))
     
  # for b in bots:
  #   img = b.img
  #   if b.direction == 0:
  #     bot_car = pygame.image.load(str(current_dir / "img" / "cars" / f"{img}.png"))
  #     screen.blit(bot_car, (b.cord[0], b.cord[1]))  
  #     b.travel()
  #   elif b.direction == 1:
  #     bot_car = pygame.image.load(str(current_dir / "img" / "cars" / f"{img}.png"))
  #     rotated_bot = pygame.transform.rotate(bot_car, 180)
  #     rect = rotated_bot.get_rect(center=(b.cord[0], b.cord[1]))
  #     screen.blit(rotated_bot, rect.topleft)  
  #     b.travel_down()
  #   if b.cord[1] + 150 < 0 or b.cord[1] - 150 > 800:
  #     bots.remove(b)
    
         
  rotated_car = pygame.transform.rotate(car, angle)
  rect = rotated_car.get_rect(center=(width // 2, width // 2))

  if y > 400 and x > 400 and y < MAP_HEIGHT - 400 and x < MAP_WIDTH - 400:  
    screen.blit(rotated_car, rect)
  else:
    if y > 400 and y < MAP_HEIGHT - 400 and x < MAP_WIDTH - 400:
      rect = rotated_car.get_rect(center=(x, 400))
      screen.blit(rotated_car, rect)
    elif y < 400 and x > 400 and x < MAP_WIDTH - 400:
      rect = rotated_car.get_rect(center=(400, y))
      screen.blit(rotated_car, rect)
    elif y > MAP_HEIGHT - 400 and x < 400:
      rect = rotated_car.get_rect(center=(x, y - (800 * 4)))
      screen.blit(rotated_car, rect)
    elif y > MAP_HEIGHT - 400 and x > 400 and x < MAP_WIDTH - 400:
      rect = rotated_car.get_rect(center=(400, y - (800 * 4)))
      screen.blit(rotated_car, rect)
    elif x > MAP_WIDTH - 400 and y > 400 and y < MAP_HEIGHT - 400:
      rect = rotated_car.get_rect(center=(x - (800 * 4), 400))
      screen.blit(rotated_car, rect)
    elif x > MAP_WIDTH - 400 and y < 400:
      rect = rotated_car.get_rect(center=(x - (800 * 4), y))
      screen.blit(rotated_car, rect)
    elif x > MAP_WIDTH - 400 and y > MAP_HEIGHT - 400:
      rect = rotated_car.get_rect(center=(x - (800 * 4), y - (800 * 4)))
      screen.blit(rotated_car, rect)
    else:
      rect = rotated_car.get_rect(center=(x, y))
      screen.blit(rotated_car, rect)
      
  rotated_rule = pygame.transform.rotate(rule, turn*150)
  rec = rotated_rule.get_rect(center=(650, 650))
      
  screen.blit(rotated_rule, rec)
  # screen.blit(d if go_to == 0 else r, (600, 400))

  pygame.display.update()