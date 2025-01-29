import pyxel
import random
import math

PLAYER_SPEED = 2
ENEMY_SPEED = 5
MAX_JUMP_POWER = 175

def __init__():
    pyxel.init(160,120)
    pyxel.load("penguin_jump.pyxres")
    pyxel.sound(0).set("c4c3c2","n","7","f",10)
    pyxel.sound(1).set("c4g4g4","p","6","n",7)
    reset()
    pyxel.run(update, draw)

def reset():
    global player_x, player_y, is_jumping, jump_power, jump_speed, player_alive, player_dir, enemies_xy, enemies_wait_time, fish_x, fish_y, score
    player_x = 70
    player_y = 114
    is_jumping = False
    jump_power = 0
    jump_speed = 10
    player_alive = True
    player_dir = "left"
    enemies_xy = [[20*i, 0] for i in range(8)]
    enemies_wait_time = [random.randint(30,210) for i in range(8)]  #1~7sec
    fish_x = 70
    fish_y = 80
    score = 0

def update():
    if player_alive:
        update_player_x()
        update_player_y()
        update_enemies()
        check_collision()
        check_fish_get()
    else:
        if pyxel.btn(pyxel.KEY_R):
            reset()

def update_player_x():
    global player_x, player_dir
    if pyxel.btn(pyxel.KEY_D):
        player_x = player_x + PLAYER_SPEED
        player_dir = "right"
    if pyxel.btn(pyxel.KEY_A):
        player_x = player_x - PLAYER_SPEED
        player_dir = "left"
    if player_x > 160 - 16:
        player_x = 144
    if player_x < 0:
        player_x = 0

def update_player_y():
    global player_y, is_jumping, jump_power, jump_speed
    GRAVITY = 1
    if is_jumping:  #ジャンプしているとき
        jump_speed = jump_speed + GRAVITY  #速度の更新
        player_y = player_y + jump_speed  #座標の更新
    elif pyxel.btn(pyxel.KEY_SPACE):
        jump_power += 8
        jump_power = min(jump_power, MAX_JUMP_POWER)  #天井に当たらないようにする
    elif pyxel.btnr(pyxel.KEY_SPACE):  #ジャンプしていないときにスペースキー押されたら
        is_jumping = True
        jump_speed = -math.sqrt(jump_power)  #初速度上向き
        jump_power = 10
    if player_y > 120 - 16:
        player_y = 104
        is_jumping = False

def update_enemies():
    global enemies_xy, enemies_wait_time
    for i in range(len(enemies_xy)):
        enemies_wait_time[i] = enemies_wait_time[i] - 1
        enemy_x, enemy_y = enemies_xy[i]
        if enemy_y < 0:
            enemy_y = enemy_y + 1
        if enemies_wait_time[i] <= 0:  #つらら落下
            enemy_y = enemy_y + ENEMY_SPEED
            if enemy_y > 132:
                enemy_y = -16
                enemies_wait_time[i] = random.randint(30,210)
        elif enemies_wait_time[i] <= 18:  #つらら震えるやつ
            if enemies_wait_time[i]%6 == 0:
                enemy_x = enemy_x + 2
            elif enemies_wait_time[i]%3 == 0:
                enemy_x = enemy_x - 2
        enemies_xy[i] = [enemy_x, enemy_y]

def check_collision():
    global player_alive, player_x, player_y, enemies_xy
    for enemy_x, enemy_y in enemies_xy:
        if (abs(player_x - enemy_x)) < 10 and (abs(player_y - enemy_y)) < 16:
            player_alive = False
            pyxel.play(0,0)

def check_fish_get():
    global fish_x, fish_y, score
    if (abs(player_x - fish_x)) < 16 and (abs(player_y - fish_y)) < 16:
        score = score + 1
        pyxel.play(0,1)
        fish_x = random.randint(0,144)
        fish_y = random.randint(16,104)

def draw():
    pyxel.cls(6)
    draw_player()
    draw_enemies()
    draw_others()

def draw_player():
    if not player_alive:
        pyxel.blt(player_x,player_y,0,32,0,16,16,6)
    else:
        if player_dir == "left":
            pyxel.blt(player_x,player_y,0,0,0,16,16,6)
        else:
            pyxel.blt(player_x,player_y,0,0,0,-16,16,6)

def draw_enemies():
    for i in range(len(enemies_xy)):
        enemy_x, enemy_y = enemies_xy[i]
        pyxel.blt(enemy_x,enemy_y,0,16,0,16,16,6)

def draw_others():
    pyxel.blt(fish_x,fish_y,0,48,0,16,16,6)
    pyxel.text(0,0,f'fish {score}',0)
    if not player_alive:
        pyxel.text(40,50,'press R to continue',0)

__init__()