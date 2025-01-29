import pyxel
import random
import math

PLAYER_SPEED = 2
ENEMY_SPEED = 1
ARRAY_KEY = [pyxel.KEY_RIGHT, pyxel.KEY_LEFT, pyxel.KEY_DOWN, pyxel.KEY_UP]  #移動キーの初期配列
FLASH_INTERVAL = 15  #点滅の周期
RADIUS = 20  #サーチライトの半径

def __init__():
    pyxel.init(160,120)
    reset()
    pyxel.run(update, draw)

def reset():
    global player_x, player_y, array_key_num, enemy_x, enemy_y, time, player_alive
    player_x = 0
    player_y = 0
    array_key_num = [0,1,2,3]
    #reset_array_key_num()  #* キー配列ぐちゃぐちゃ
    enemy_x = 100
    enemy_y = 100
    time = 0
    player_alive = True

def update():
    if player_alive == True:
        update_player()
        check_collision()
        #update_enemy_easy()  #* 敵が追尾(2種類で実装)
        #update_timer()  #* 時間制限
    else:
        if pyxel.btnp(pyxel.KEY_SPACE):
            reset()

def reset_array_key_num():
    #array_key_numを、0~3が1つずつ入った配列にする
    global array_key_num
    new_array_key_num = []
    while len(new_array_key_num) < 4:
        rand = random.randint(0,3)
        if rand in new_array_key_num:  #重複がないか確認
            continue
        new_array_key_num.append(rand)
    array_key_num = new_array_key_num  #array_key_numを更新

def update_player():
    global player_x, player_y
    if pyxel.btn(ARRAY_KEY[array_key_num[0]]):
        player_x = player_x + PLAYER_SPEED
    elif pyxel.btn(ARRAY_KEY[array_key_num[1]]):
        player_x = player_x - PLAYER_SPEED
    if pyxel.btn(ARRAY_KEY[array_key_num[2]]):
        player_y = player_y + PLAYER_SPEED
    elif pyxel.btn(ARRAY_KEY[array_key_num[3]]):
        player_y = player_y - PLAYER_SPEED
    if player_x > pyxel.width - 16:
        player_x = pyxel.width - 16
    if player_x < 0:
        player_x = 0
    if player_y > pyxel.height - 16:
        player_y = pyxel.height - 16
    if player_y < 0:
        player_y = 0

def check_collision():
    global player_alive
    if enemy_x-20 < player_x < enemy_x+5 and enemy_y-20 < player_y < enemy_y+5:
        player_alive = False

def update_enemy_easy():
    global enemy_x, enemy_y
    if enemy_x < player_x + 8:
        enemy_x = enemy_x + ENEMY_SPEED
    else:
        enemy_x = enemy_x - ENEMY_SPEED
    if enemy_y < player_y + 8:
        enemy_y = enemy_y + ENEMY_SPEED
    else:
        enemy_y = enemy_y - ENEMY_SPEED

def update_enemy_hard():
    global enemy_x, enemy_y
    #速度一定で、xy方向に分解
    theta = math.atan(abs(enemy_y - player_y)/abs(enemy_x - player_x))
    if enemy_x < player_x + 8:
        enemy_dir_x = 1
    else:
        enemy_dir_x = -1
    if enemy_y < player_y + 8:
        enemy_dir_y = 1
    else:
        enemy_dir_y = -1
    enemy_x = enemy_x + enemy_dir_x*ENEMY_SPEED*math.cos(theta)
    enemy_y = enemy_y + enemy_dir_y*ENEMY_SPEED*math.sin(theta)

def update_timer():
    global time, player_alive
    #経過フレーム数(変数に入れておけばresetかけても大丈夫)
    time = time + 1
    if time > 10*30:  #10秒後(1秒が30フレーム)
        player_alive = False

def draw():
    if player_alive == True:
        draw_normal()
        #draw_flash()  #* 敵が点滅
        #draw_search_light()  #* サーチライト
    else:
        pyxel.cls(0)
        pyxel.text(0,0,'press space to retry',7)

def draw_normal():
    pyxel.cls(0)
    pyxel.rect(player_x, player_y, 16, 16, 9)
    pyxel.circ(enemy_x, enemy_y, 4, 12)
    pyxel.text(100, 0, f"time: {time//30}", 7)

def draw_flash():
    pyxel.cls(0)
    pyxel.rect(player_x, player_y, 16, 16, 9)
    pyxel.text(100, 0, f"time: {time//30}", 7)
    #今は7フレーム表示、8フレーム非表示の15フレーム周期の点滅
    if pyxel.frame_count%FLASH_INTERVAL < 7:
        pyxel.circ(enemy_x, enemy_y, 4, 12)

def draw_search_light():
    pyxel.cls(13)
    pyxel.rect(player_x, player_y, 16, 16, 9)
    pyxel.circ(enemy_x, enemy_y, 4, 12)
    #座標(x,y)がプレイヤーを中心とした円の外なら、黒く塗りつぶす
    for x in range(pyxel.width):
        for y in range(pyxel.height):
            if (player_x + 8 - x)**2 + (player_y + 8 - y)**2 > RADIUS**2:
                pyxel.pset(x,y,0)
    pyxel.text(100, 0, f"time: {time//30}", 7)

__init__()