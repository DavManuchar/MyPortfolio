import math


def distance(x,y,x1,y1):
  f = math.sqrt((x1-x)**2 + (y1-y)**2)
  return f

def arr(arr,x,y,matrix_w,matrix_h): 
    if(arr == "up"):
      x = x - 1
      if(x >= 0 and x <= matrix_h):
        return (x,y)
      else:
        return False
    elif arr == "down":
      x = x + 1
      if(x <= matrix_h and x >= 0):
        return (x,y)
      else:
        return False
    elif arr == "right":
      y = y + 1
      if(y <= matrix_w and y >= 0):
        return (x,y)
      else:
        return False
    elif arr == "left":
      y = y - 1
      if(y >= 0 and y <= matrix_w):
        return (x,y)
      else:
        return False
      
def a_star(map,start,goal):
  matrix_w = len(map[0]) - 1
  matrix_h= len(map) - 1
  
  x = start[0]
  y = start[1]
  x1 = goal[0]
  y1 = goal[1]
  
  krug = 0
  way = []
  before = []
  v = []
  
  wayy = True
  run = True
  
  while run == True and (x,y) not in before:
    put = []
    cord = []
    
    up = arr("up",x,y,matrix_w,matrix_h)
    down = arr("down",x,y,matrix_w,matrix_h)
    left = arr("left",x,y,matrix_w,matrix_h)
    right = arr("right",x,y,matrix_w,matrix_h)

    if up != False and map[up[0]][up[1]] != 1 and (up[0],up[1]) not in before and (up[0],up[1]) not in v:
      up_cash = math.floor(distance(up[0],up[1],x1,y1) * 10) 
      cord.append(up)
      put.append(up_cash)
    else: 
      up_cash = False
    if down != False and map[down[0]][down[1]] != 1 and (down[0],down[1]) not in before and (down[0],down[1]) not in v:
      down_cash = math.floor(distance(down[0],down[1],x1,y1) * 10)
      cord.append(down)
      put.append(down_cash)
    else: 
      down_cash = False
    if left != False and map[left[0]][left[1]] != 1  and (left[0],left[1]) not in before and (left[0],left[1]) not in v:
      left_cash = math.floor(distance(left[0],left[1],x1,y1) * 10)
      cord.append(left)
      put.append(left_cash)
    else: 
      left_cash = False
    if right != False and map[right[0]][right[1]] != 1  and (right[0],right[1]) not in before and (right[0],right[1]) not in v:
      right_cash = math.floor(distance(right[0],right[1],x1,y1) * 10)
      cord.append(right)
      put.append(right_cash)
    else: 
      right_cash = False
      
    if (start[0],start[1]) in v:
      wayy = False
      run = False  
    
    if len(put) > 0:
      close = min(put)
      index = put.index(close)
      before.append((x,y))
      x = cord[index][0]
      y = cord[index][1]
    else:
      krug += 1
      v.append((x,y))
      before = []
      x = start[0]
      y = start[1]

    if close == 0:
      way = before
      run = False 

  if wayy == True:
    return way
  else:
    return "No way...:(" 
    

# map = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 1, 1, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 1, 0, 0]
# ]

# start = (2, 1)
# goal = (2, 4)

# print(a_star(map,start,goal))
