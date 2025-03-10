import tkinter as tk
import random
from PIL import Image, ImageTk
from tkinter import Canvas
import pygame
from porc import *
import random

root = tk.Tk()
root.title("Sopyor")
root.geometry("500x600")
root.resizable(False,False)


pygame.init()

canvas = Canvas(bg="#4a752c",highlightthickness=0, width=500, height=600)
canvas.place(x=0, y=0)

cliks = 0
bold = []
game = True
run = True

was = []
place_count = 0

matrix = [[0 for _ in range(10)] for _ in range(10)]

def pos(x, y):
  global running
  running = True
  update_timer()
  click_pos = find_neighbors(matrix, x, y)
  
  i = 0
  while i < 20:
    m = random.randint(0, 9)
    n = random.randint(0, 9)

    if matrix[m][n] == 0 and (m, n) not in click_pos:
        matrix[m][n] = 1
        i += 1
  zero((x, y))
  


def start():
  if game == True:
    global flag_photo, time_photo, t, current_time, timer
    
    flag_image_path = "C:/py/sopyor/img/flag.png"
    flag_img = Image.open(flag_image_path).resize((60, 60))
    flag_photo = ImageTk.PhotoImage(flag_img)
    canvas.create_image(100, 20, anchor="nw", image=flag_photo)
    
    t = canvas.create_text(180,50, text=20, fill="white",anchor="center", font=('Helvetica', 20, "bold"))
    
    time_image_path = "C:/py/sopyor/img/time.png"
    time_img = Image.open(time_image_path).resize((60, 60))
    time_photo = ImageTk.PhotoImage(time_img)
    canvas.create_image(300, 20, anchor="nw", image=time_photo)
    
    current_time = 0
    
    timer = canvas.create_text(380,50, text=str(current_time), fill="white",anchor="center", font=('Helvetica', 20, "bold"))
    
    
    col = 0
    w = 0
    h = 100
    id = 0
    for i in range(10):
      col = 1 if col == 0 else 0
      for j in range(10):
        if col == 0:
          a = canvas.create_rectangle(w,h,w+50,h+50, fill="#aad751", outline="")
          text = canvas.create_text(w+25,h+25, text="", fill="red",anchor="center", font=('Helvetica', 15, "bold"))
          
          col = 1
  
        else:
          a = canvas.create_rectangle(w,h,w+50,h+50, fill="#a2d149", outline="")
          text = canvas.create_text(w+25,h+25, text="", fill="red",anchor="center", font=('Helvetica', 15, "bold"))
          z = f"({i},{j})"
          z = eval(z)
          bold.append(z)
          col = 0
          
        tag = (f"({i},{j})")
        tag_text = (f"{i}_{j}")
        canvas.itemconfig(a, tags=tag)
        canvas.itemconfig(text, tags=tag_text)
  
        canvas.tag_bind(tag, "<Button-1>", lambda event, t=tag: on_rectangle_click(event, t))
        canvas.tag_bind(tag, "<Button-3>", lambda event, t=tag: flag(event, t))
              
          
        w += 50
      h += 50
      w = 0
      
  else:
    col = 0
    w = 0
    h = 100
    for i in range(10):
      col = 1 if col == 0 else 0
      for j in range(10):
        if col == 0:
          a = canvas.create_rectangle(w,h,w+50,h+50, fill="#e5c29f", outline="")        
          col = 1
        else:
          a = canvas.create_rectangle(w,h,w+50,h+50, fill="#d7b899", outline="")
          col = 0    
        w += 50
      h += 50
      w = 0
    text = canvas.create_text(250,300, text="Victory", fill="red",anchor="center", font=('Helvetica', 35, "bold"))
  
def update_timer():
    global current_time

    if running == True:
      current_time += 1
      
      canvas.itemconfig(timer, text=str(current_time))
  
      canvas.after(1000, update_timer)
  
def flag(event, cord):
    point = eval(cord)
    tag = f"({point[0]},{point[1]})"
    tag_text = f"{point[0]}_{point[1]}"
        
    text = canvas.find_withtag(tag_text)
    canvas.itemconfig(text, text="<|", fill="red")
  
def find_bombs(matrix, x, y):
  neigh = find_neighbors(matrix, x, y)
  count = 0
  
  for point in neigh:
    if matrix[point[0]][point[1]] == 1:
      count += 1
      
  return count
      
    
def zero(cord):
  global cliks, place_count, game, running
  all_points = find_connected_zeros(matrix, cord)
  
  for i in range(len(all_points)):
    place_count += 1
    point = all_points[i]
    tag = f"({point[0]},{point[1]})"
    tag_text = f"{point[0]}_{point[1]}"
        
    rectangles = canvas.find_withtag(tag)
    text = canvas.find_withtag(tag_text)
    canvas.tag_unbind(tag, "<Button-1>")
    tag = eval(tag)
    if tag not in was:
      was.append(tag)
      cliks += 1
    if cliks == 80:
      game = False
      running = False
      start()
    for rect in rectangles:
      bombs = find_bombs(matrix, point[0], point[1])
      if tag in bold:
        if bombs == 0:
          canvas.itemconfig(rect, fill="#d7b899")
          canvas.itemconfig(text, text="")
          
        else:
          canvas.itemconfig(rect, fill="#d7b899")
          place_number(bombs, text)
            
      else:
        if bombs == 0:
          canvas.itemconfig(rect, fill="#e5c29f")
          canvas.itemconfig(text, text="")
        else:
          canvas.itemconfig(rect, fill="#e5c29f")
          place_number(bombs, text)
  print(cliks)
  
def place_number(bombs, text):
  if bombs == 1: 
    canvas.itemconfig(text, text=bombs, fill="#1976d2")
  elif bombs == 2: 
    canvas.itemconfig(text, text=bombs, fill="#388e3c")
  elif bombs == 3: 
    canvas.itemconfig(text, text=bombs, fill="#d32f2f")
  elif bombs == 4: 
    canvas.itemconfig(text, text=bombs, fill="#7b1fa2")
  elif bombs == 5: 
    canvas.itemconfig(text, text=bombs, fill="red")
  elif bombs == 5: 
    canvas.itemconfig(text, text=bombs, fill="black")

def press(point):
  global cliks, place_count, game, run, running
  if run == True:
    
    bombs = find_bombs(matrix, point[0], point[1])
    if bombs == 0:
      zero((point[0], point[1]))
    else:
      place_count += 1
      tag = f"({point[0]},{point[1]})"
      tag_text = f"{point[0]}_{point[1]}"
          
      rectangles = canvas.find_withtag(tag)
      text = canvas.find_withtag(tag_text)
      canvas.tag_unbind(tag, "<Button-1>")
      tag = eval(tag)
      if tag not in was:
        was.append(tag)
        cliks += 1
      if cliks == 80:
        game = False
        running = False
        start()
      print(cliks)
      if tag in bold:
        if bombs == 0:
          canvas.itemconfig(rectangles, fill="#d7b899")
          canvas.itemconfig(text, text="")
        else:
          canvas.itemconfig(rectangles, fill="#d7b899")
          place_number(bombs, text)      
      else:
        if bombs == 0:
          canvas.itemconfig(rectangles, fill="#e5c29f")
          canvas.itemconfig(text, text="")
        else:
          canvas.itemconfig(rectangles, fill="#e5c29f")
          place_number(bombs, text)

def bomb(tag):
  global running, run
  if run == True:
    tag_text = f"{tag[1]}_{tag[3]}"
    text = canvas.find_withtag(tag_text)
    canvas.itemconfig(tag, fill="black")
    canvas.itemconfig(text, text="*", fill="white")
    running = False
    run = False

def on_rectangle_click(event, tag):
  
  cordinate = eval(tag)
  
  if cliks == 0:
    pos(cordinate[0], cordinate[1])
  else:
    if matrix[cordinate[0]][cordinate[1]] == 0:
      press(cordinate)
    else:
      bomb(tag)
  



if __name__ == "__main__":
  start()

root.mainloop()