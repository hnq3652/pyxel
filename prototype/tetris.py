import pyxel
import random

DOT_SIZE = 8

O_MINO = [[1,1], [1,1]]
T_MINO = [[1,1,1], [0,1,0], [0,0,0]]
L_MINO = [[1,0,0], [1,0,0], [1,1,0]]
J_MINO = [[0,1,0], [0,1,0], [1,1,0]]
I_MINO = [[1,0,0,0], [1,0,0,0], [1,0,0,0], [1,0,0,0]]
S_MINO = [[0,1,1], [1,1,0], [0,0,0]]
Z_MINO = [[1,1,0], [0,1,1], [0,0,0]]
MINOS = [O_MINO, T_MINO, L_MINO, J_MINO, I_MINO, S_MINO, Z_MINO]
MINOS_COLOR = [i for i in range(1,8)]

def __init__():
    pyxel.init(DOT_SIZE*15,DOT_SIZE*20)
    reset()
    pyxel.run(update, draw)

def reset():
    global now_mino, now_mino_pattern, mino_x, mino_y, mino_stop_time, next_mino, stacked_mino, heights
    now_mino = random.randint(0,6)
    now_mino_pattern = MINOS[now_mino]
    mino_x, mino_y = 48, 0
    mino_stop_time = 15
    next_mino = random.randint(0,6)
    stacked_mino = [[0 for j in range(15)] for i in range(21)]
    stacked_mino[-1] = [1 for i in range(15)]
    heights = [160 for i in range(15)]

def update():
    if mino_stop_time >= 0:
        update_mino()
    else:
        stack_mino()
        check_line()
        create_new_mino()
    if pyxel.btnp(pyxel.KEY_0):  #! for debug
        reset()

def update_mino():
    global now_mino_pattern, mino_x, mino_y, mino_stop_time
    if pyxel.btnp(pyxel.KEY_SPACE):
        rotate()
        if not check_collision(mino_x, mino_y):
            rotate()
            rotate()
            rotate()
    else:
        dy = 0
        ratio = 1
        if pyxel.btn(pyxel.KEY_DOWN):
            ratio = 3
        dy = 1*ratio
        if check_collision(mino_x, mino_y+dy):
            mino_y = mino_y + dy
            dx = 0
            if pyxel.btnp(pyxel.KEY_LEFT):
                dx = -DOT_SIZE
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                dx = DOT_SIZE
            if check_collision(mino_x+dx, mino_y):
                mino_x = mino_x + dx
        else:
            mino_stop_time -= 1

def check_collision(x,y):
    for i in range(len(now_mino_pattern)):
        for j in range(len(now_mino_pattern)):
            if now_mino_pattern[i][j] != 0:
                if heights[(x + DOT_SIZE*j)//DOT_SIZE] < y + DOT_SIZE*(i+1):
                    return False
    return True

def rotate():
    global now_mino_pattern
    rotated_mino = [[0 for j in range(len(now_mino_pattern))] for i in range(len(now_mino_pattern))]
    for i in range(len(now_mino_pattern)):
        for j in range(len(now_mino_pattern)):
            rotated_mino[j][len(now_mino_pattern)-i-1] = now_mino_pattern[i][j]
    now_mino_pattern = rotated_mino

def stack_mino():
    global stacked_mino, height
    for i in range(len(now_mino_pattern)):
        for j in range(len(now_mino_pattern)):
            if now_mino_pattern[i][j] == 1:
                stacked_mino[(mino_y + DOT_SIZE*i)//DOT_SIZE][(mino_x + DOT_SIZE*j)//DOT_SIZE] = MINOS_COLOR[now_mino]
                if heights[(mino_x + DOT_SIZE*j)//DOT_SIZE] > mino_y + DOT_SIZE*i:
                    heights[(mino_x + DOT_SIZE*j)//DOT_SIZE] = mino_y + DOT_SIZE*i

def check_line():
    global stacked_mino, heights
    for k in range(4):
        for i in range(len(stacked_mino)-1):
            clear = True
            for j in range(len(stacked_mino[i])):
                if stacked_mino[i][j] == 0:
                    clear = False
            if clear == True:
                stacked_mino = [[0 for j in range(15)]] + stacked_mino[:i] + stacked_mino[i+1:]
                for j in range(len(stacked_mino[i])):
                    heights[j] += DOT_SIZE
                break

def create_new_mino():
    global now_mino, now_mino_pattern, mino_x, mino_y, mino_stop_time, next_mino
    now_mino = next_mino
    now_mino_pattern = MINOS[now_mino]
    mino_x, mino_y = 48, 0
    mino_stop_time = 15
    next_mino = random.randint(0,6)

def draw():
    pyxel.cls(0)
    for i in range(len(stacked_mino)):
        for j in range(len(stacked_mino[i])):
            pyxel.rect(DOT_SIZE*j, DOT_SIZE*i, DOT_SIZE, DOT_SIZE, stacked_mino[i][j])
    for i in range(len(now_mino_pattern)):
        for j in range(len(now_mino_pattern)):
            if now_mino_pattern[i][j] == 1:
                pyxel.rect(mino_x + DOT_SIZE*j, mino_y + DOT_SIZE*i, DOT_SIZE, DOT_SIZE, MINOS_COLOR[now_mino])

__init__()

#! 右端超えるとエラー吐く(超えられないようにするべき)
#todo 次のやつ表示
#todo ゲームオーバー
#todo 落下点を予測表示
#todo 回転の中心ばらばら(T-Spinなどができない)