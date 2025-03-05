from pathlib import Path
import pygame
import random
import sqlite3

current_dir = Path(__file__).parent


def execute_query(query, params=()):
  with sqlite3.connect(current_dir / "db.db") as connection:
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    return cursor.fetchall()
  
nicknames = execute_query("SELECT nickname FROM users")

passwords = execute_query("SELECT password FROM users")

pygame.init()

screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption("Pairs")
ico =  pygame.image.load(str(current_dir / "img" / "poker.ico"))
pygame.display.set_icon(ico)

card_cordinates = [
  [(50,280), (200,280), (350,280), (500,280), (650,280)],
  [(50,430), (200,430), (350,430), (500,430), (650,430)],
  [(50,580), (200,580), (350,580), (500,580), (650,580)],
  [(50,730), (200,730), (350,730), (500,730), (650,730)]
]

player_levl = 1

background = pygame.image.load(str(current_dir / "img" / "background.jpg"))


folder_path = Path(str(current_dir / "img" / "animals"))
file_names = [f.name for f in folder_path.iterdir() if f.is_file()]

animals_cards = []
all_cards_cordinate = []
all_cards_bulian = []

user_id = 0

first_card = 99
second_card = 99

click = True
game = False
game_start = False
sound = True
register = False
in_game = False 
interfais = True
podium_interfais = False

fon_sound = pygame.mixer.Sound(str(current_dir / "audio" / "fon.mp3"))
victory_sound = pygame.mixer.Sound(str(current_dir / "audio" / "victory.wav"))
start_sound = pygame.mixer.Sound(str(current_dir / "audio" / "start.wav"))

chanal0 = pygame.mixer.Channel(0)
chanal1 = pygame.mixer.Channel(1)
chanal2 = pygame.mixer.Channel(2)
chanal3 = pygame.mixer.Channel(3)

sound_on = pygame.image.load(str(current_dir / "img" / "sound-on.png"))
sound_off = pygame.image.load(str(current_dir / "img" / "sound-off.png"))
back = pygame.image.load(str(current_dir / "img" / "back.png"))
podium = pygame.image.load(str(current_dir / "img" / "podium.png"))

button_rect = pygame.Rect(300, 550, 200, 100) 

font = pygame.font.Font(None, 46) 
levl_font = pygame.font.Font(None, 70) 
log_font = pygame.font.Font(None, 25) 
input_font = pygame.font.Font(None, 46) 

ROTATE_TIMER = pygame.USEREVENT + 1
WIN_TIMER = pygame.USEREVENT + 2


class levl:
  def __init__(self, lvl ,cord, animals_count):
    global animals_cards, game, all_cards_bulian, first_card, second_card
    game = False
    animals_cards = []
    all_cards_bulian = []
    
    first_card = 99
    second_card = 99
    
    self.lvl = lvl
    self.cord = cord
    self.animals_count = animals_count
    
    sec_an_cards = []
    
    for i in range(animals_count):
      sec_an_cards.append(file_names[i])
      
    for i in range(animals_count * 2):
      id = random.randint(0, len(sec_an_cards)-1 if len(sec_an_cards) > 0 else 0)
      if sec_an_cards[id] not in animals_cards:
        animals_cards.append(sec_an_cards[id])
        all_cards_cordinate.append((cord[i][0], cord[i][1], cord[i][0] + 100, cord[i][1] + 100))
        all_cards_bulian.append(0)
      else:
        animals_cards.append(sec_an_cards[id])
        all_cards_cordinate.append((cord[i][0], cord[i][1], cord[i][0] + 100, cord[i][1] + 100))
        all_cards_bulian.append(0)
        sec_an_cards.pop(id)
    
  
  def load(self, cord):
    global all_cards_bulian, first_card, second_card, click, all_cards_bulian, all_cards_cordinate, player_levl, game
    if first_card == 99 and second_card == 99:
      first_card = cord
      all_cards_bulian[cord] = 1 
    else:
      click = False
      second_card = cord
      all_cards_bulian[cord] = 1
      if animals_cards[first_card] == animals_cards[second_card]:
        first_card = 99
        second_card = 99
        if 0 in all_cards_bulian:
          click = True
        else:
          click = True
          return True
      else: 
        pygame.time.set_timer(ROTATE_TIMER, 1000)
      
  def rotate_load(self, cord):
    p = pygame.image.load(str(current_dir / "img" / "rotate.png"))
    for i in range(len(animals_cards)):
      if all_cards_bulian[i] == 0:
        screen.blit(p, (cord[i][0], cord[i][1]))
      else:
        screen.blit(pygame.image.load(str(current_dir / "img" / "animals" / animals_cards[i])), (cord[i][0], cord[i][1]))
      
      
name_box = pygame.Rect(200, 400, 400, 40)
password_box = pygame.Rect(200, 460, 400, 40)


name_text = "" 
password_text = "" 

name_placeholder = "Nickname"
password_placeholder = "Password(min 8)"

name_active = False
password_active = False

name_check = True
password_check = True

log_reg = log_font.render("register/ log in", True, (17, 42, 70))
log_rect = log_reg.get_rect(center=(260, 520))

chanal0.play(fon_sound, loops=-1)

running = True
while running:
  def choose_player_level():
    if player_levl == 1:
      levl1 = levl(player_levl, [(200,430), (500,430), (200,580), (500,580)], 2) 
    elif player_levl == 2:
      levl1 = levl(player_levl, [(200,430), (500,430), (200,580), (500,580), (350,430), (350,580)], 3)
    elif player_levl == 3:
      levl1 = levl(player_levl, [(200,430), (500,430), (200,580), (500,580), (350,430), (350,580), 
                                 (200,280), (350,280), (500,280), (200,730), (350,730), (500,730)], 6)
    else:
      for_lvl = []
    
      for i in range(len(card_cordinates)):
        for j in range(len(card_cordinates[i])):
          for_lvl.append(card_cordinates[i][j])
        
      levl1 = levl(player_levl, for_lvl, 10)

    return levl1

  screen.blit(background, (0, 0))

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
          
          
      if event.type == pygame.KEYDOWN and name_active == True:
        if event.key == pygame.K_BACKSPACE:
          name_text = name_text[:-1]
        else:
          name_text += event.unicode
          
      if event.type == pygame.KEYDOWN and password_active == True:
        if event.key == pygame.K_BACKSPACE:
          password_text = password_text[:-1]
        else:
          password_text += event.unicode
          
      if event.type == ROTATE_TIMER:
        all_cards_bulian[first_card] = 0
        all_cards_bulian[second_card] = 0 
        first_card = 99
        second_card = 99
        click = True
        pygame.time.set_timer(ROTATE_TIMER, 0)
        
      if event.type == WIN_TIMER:
        game = True
        pygame.time.set_timer(WIN_TIMER, 0)

      if event.type == pygame.MOUSEBUTTONDOWN:
        if name_box.collidepoint(event.pos) and game_start == False:
          name_active = True
        else:
          name_active = False
          
        if password_box.collidepoint(event.pos) and game_start == False:
          password_active = True
        else:
          password_active = False
          
        if log_rect.collidepoint(event.pos) and game_start == False:
          if register == False:
            register = True
          else:
            register = False
                
        if button_rect.collidepoint(event.pos) and game_start == False and in_game == False:
          if len(name_text) > 0 and len(password_text) > 0:
            if register == False:
              existing_user = execute_query("SELECT id FROM users WHERE nickname = ?", (name_text,))
              if existing_user:
                name_check = False
                break
              elif len(password_text) < 8:
                password_check = False
                break
              else:
                connection = sqlite3.connect(current_dir / "db.db")
                cursor = connection.cursor()
                
                name_check = True
                cursor.execute("INSERT INTO users (nickname, password, level) VALUES (?, ?, ?)", (name_text, password_text, 1))
                
                connection.commit()
                existing_user = execute_query("SELECT id FROM users WHERE nickname = ?", (name_text,))
                
                if sound == True:
                  chanal1.play(start_sound)
                game_start = True
                in_game = True
                game = True
                interfais = False
                player_levl = 1
                user_id = existing_user[0][0]
            else:
              existing_user = execute_query("SELECT id FROM users WHERE nickname = ?", (name_text,))
              if not existing_user:
                name_check = False
              else:
                user_id = existing_user[0][0]
                all_query = execute_query("SELECT * FROM users WHERE id = ?", (user_id,))
                if password_text != all_query[0][2]:
                  user_id = 0
                  password_check = False
                else:
                  if sound == True:
                    chanal1.play(start_sound)
                    
                  player_levl = all_query[0][3]
                  game_start = True
                  in_game = True
                  interfais = False
                  game = True
                  
        x, y = event.pos
        
        if 10 <= x <= 40 and 10 <= y <= 40:
          if sound == True:
            sound = False
            pygame.mixer.stop()
          else:
            sound = True
            chanal0.play(fon_sound, loops=-1)

        elif 10 <= x <= 60 and 210 <= y <= 260:
          if game_start == False and in_game == True:
            game_start = True 
            click = True
            podium_interfais = False
          elif in_game == False and game_start == False:
            interfais = True 
            podium_interfais = False
            click = True
          elif in_game == True and game_start == True:
            game_start = False
            in_game = False
            interfais = True
            click = True
            podium_interfais = False
            all_cards_bulian = []
            all_cards_cordinate = []

        elif 740 <= x <= 790 and 220 <= y <= 270:
          podium_interfais = True
          if game_start == True and in_game == True:
            game_start = False 
            click = False
          elif game == False and game_start == False:
            interfais = False
            click = False 

        
        if in_game == True:
          for i in range(len(all_cards_cordinate)):
            if all_cards_cordinate[i][0] <= x <= all_cards_cordinate[i][2] and all_cards_cordinate[i][1]<= y <= all_cards_cordinate[i][3] and all_cards_bulian[i] == 0 and click == True:
              a = lavel_proces.load(i)
              if a == True:
                player_levl += 1
                execute_query("UPDATE users SET level = ? WHERE id = ?", (player_levl, user_id))
                all_cards_cordinate = []
                if sound == True:
                  chanal2.play(victory_sound)
                pygame.time.set_timer(WIN_TIMER, 2000) 
                break
      
  if game == True:
    lavel_proces = choose_player_level()

  if game_start == True: 
    lavel_proces.rotate_load(lavel_proces.cord)
  
    
  text = levl_font.render(f"{player_levl}", True, (17, 42, 70))
  text_rect = text.get_rect(center=(690, 80))  
  screen.blit(text, text_rect)
  
  screen.blit(back, (10, 210))
  screen.blit(podium, (740, 220))

  if sound == True:
    screen.blit(sound_on, (10, 10))
  else:
    screen.blit(sound_off, (10, 10))
  
  if game_start == False and game == False and interfais == True: 
    def regist():
      text = levl_font.render("Register" if register == False else "Log in", True, (17, 42, 70))
      text_rect = text.get_rect(center=(300, 350))  
      screen.blit(text, text_rect)
      # NAME
      pygame.draw.rect(screen, (255,255,255), name_box)
      pygame.draw.rect(screen, (255,255,255) if name_check == True else (255,0,0), name_box, 2)
      
      if not name_text and not name_active:
        placeholder_surface = input_font.render(name_placeholder, True, (125, 125, 125))
        screen.blit(placeholder_surface, (name_box.x + 5, name_box.y + 5))
      else:
        text_surface = input_font.render(name_text, True, (0,0,0))
        screen.blit(text_surface, (name_box.x + 5, name_box.y + 5))
      
      # PASSWORD
      pygame.draw.rect(screen, (255,255,255), password_box)
      pygame.draw.rect(screen, (255,255,255) if password_check == True else (255,0,0), password_box, 2)
      
      if not password_text and not password_active:
        placeholder_surface = input_font.render(password_placeholder, True, (125, 125, 125))
        screen.blit(placeholder_surface, (password_box.x + 5, password_box.y + 5))
      else:
        text_surface = input_font.render(password_text, True, (0,0,0))
        screen.blit(text_surface, (password_box.x + 5, password_box.y + 5))
    
    pygame.draw.rect(screen, (85, 157, 255), button_rect, border_radius=20)
    text = font.render("Register" if register == False else "Log in", True, (255,255,255))
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
      
    screen.blit(log_reg, log_rect)

    regist()
    
  if podium_interfais == True:
    top_users = execute_query("SELECT id FROM users ORDER BY level DESC LIMIT 5")
    top1 = pygame.image.load(str(current_dir / "img" / "1.png"))
    top2 = pygame.image.load(str(current_dir / "img" / "2.png"))
    top3 = pygame.image.load(str(current_dir / "img" / "3.png"))

    t_rang = log_font.render('Rang', True, (0,0,0))
    screen.blit(t_rang, (200, 300))

    t_id = log_font.render('Id', True, (0,0,0))
    screen.blit(t_id, (300, 300))

    t_name = log_font.render('Nickname', True, (0,0,0))
    screen.blit(t_name, (400, 300))

    t_level = log_font.render('Level', True, (0,0,0))
    screen.blit(t_level, (550, 300))
    
    h = 350
    for i in range(5):
      user = execute_query("SELECT * FROM users WHERE id = ?", (top_users[i][0], ))

      if i + 1 == 1:
        screen.blit(top1, (200, h))

        text_id = font.render(f'{user[0][0]}', True, (0,0,0))
        screen.blit(text_id, (300, h))

        text_name = font.render(f'{user[0][1]}', True, (0,0,0))
        screen.blit(text_name, (400, h))

        text_level = font.render(f'{user[0][3]}', True, (0,0,0))
        screen.blit(text_level, (550, h))

      elif i + 1 == 2:
        screen.blit(top2, (200, h))

        text_id = font.render(f'{user[0][0]}', True, (0,0,0))
        screen.blit(text_id, (300, h))

        text_name = font.render(f'{user[0][1]}', True, (0,0,0))
        screen.blit(text_name, (400, h))

        text_level = font.render(f'{user[0][3]}', True, (0,0,0))
        screen.blit(text_level, (550, h))
        
      elif i + 1 == 3:
        screen.blit(top3, (200, h))

        text_id = font.render(f'{user[0][0]}', True, (0,0,0))
        screen.blit(text_id, (300, h))

        text_name = font.render(f'{user[0][1]}', True, (0,0,0))
        screen.blit(text_name, (400, h))

        text_level = font.render(f'{user[0][3]}', True, (0,0,0))
        screen.blit(text_level, (550, h))
      else:
        text_level = font.render(f'{i + 1}', True, (0,0,0))
        screen.blit(text_level, (200, h))

        text_id = font.render(f'{user[0][0]}', True, (0,0,0))
        screen.blit(text_id, (300, h))

        text_name = font.render(f'{user[0][1]}', True, (0,0,0))
        screen.blit(text_name, (400, h))

        text_level = font.render(f'{user[0][3]}', True, (0,0,0))
        screen.blit(text_level, (550, h))

      h += 100

    
    

  pygame.display.flip()

pygame.quit() 
