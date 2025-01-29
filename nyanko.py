import pyxel
import random

def __init__():
    pyxel.init(160,120)
    reset()
    pyxel.run(update, draw)

def reset():
    global ally_x, ally_hp, enemies_x, enemies_hp, player_alive, enemy_alive, coin, level
    ally_x = []
    ally_hp = []
    enemies_x = []
    enemies_hp = []
    player_alive = True
    enemy_alive = True
    coin = 100
    level = 1

def update():
    if player_alive == True and enemy_alive == True:
        get_coin()
        summon_ally()
        update_ally()
        summon_enemies()
        update_enemies()
        check_collision()
        check_win()
    else:
        if pyxel.btn(pyxel.KEY_R):
            reset()

def get_coin():
    global coin
    if pyxel.frame_count%30 == 0:
        coin = coin + level

def summon_ally():
    global ally_x, ally_hp, coin, level
    if pyxel.btnp(pyxel.KEY_1) and coin >= 3:
        ally_x.append(10)
        ally_hp.append(10)
        coin = coin - 3
    elif pyxel.btnp(pyxel.KEY_2) and coin >= 5:
        ally_x.append(10)
        ally_hp.append(20)
        coin = coin - 5
    elif pyxel.btnp(pyxel.KEY_0) and coin >= level*10:
        level = level + 1
        coin = coin - level*10

def update_ally():
    global ally_x
    for i in range(len(ally_x)):
        ally_x[i] = ally_x[i] + 1

def summon_enemies():
    global enemies_x, enemies_hp
    if pyxel.frame_count%(30*5) == 0:
        enemies_x.append(150)
        enemies_hp.append(random.randint(5,30))

def update_enemies():
    global enemies_x
    for j in range(len(enemies_x)):
        enemies_x[j] = enemies_x[j] - 1

def check_collision():
    global ally_x, ally_hp, enemies_x, enemies_hp
    new_ally_x, new_ally_hp, new_enemies_x, new_enemies_hp = [], [], [], []
    for i in range(len(ally_x)):
        for j in range(len(enemies_x)):
            if abs(ally_x[i] - enemies_x[j]) < 8 and ally_hp[i] != 0 and enemies_hp[j] != 0:
                if ally_hp[i] > enemies_hp[j]:
                    ally_hp[i] = ally_hp[i] - enemies_hp[j]
                    enemies_hp[j] = -1
                elif enemies_hp[j] > ally_hp[i]:
                    enemies_hp[j] = enemies_hp[j] - ally_hp[i]
                    ally_hp[i] = -1
                else:
                    ally_hp[i] = -1
                    enemies_hp[j] = -1
    for i in range(len(ally_x)):
        if ally_hp[i] != -1:
            new_ally_x.append(ally_x[i])
            new_ally_hp.append(ally_hp[i])
    for j in range(len(enemies_x)):
        if enemies_hp[j] != -1:
            new_enemies_x.append(enemies_x[j])
            new_enemies_hp.append(enemies_hp[j])
    ally_x = new_ally_x
    ally_hp = new_ally_hp
    enemies_x = new_enemies_x
    enemies_hp = new_enemies_hp

def check_win():
    global player_alive, enemy_alive
    for i in range(len(ally_x)):
        if ally_x[i] > 150:
            enemy_alive = False
    for j in range(len(enemies_x)):
        if enemies_x[j] < 10:
            player_alive = False

def draw():
    pyxel.cls(6)
    if player_alive == True and enemy_alive == True:
        for i in range(len(ally_x)):
            pyxel.rect(ally_x[i], 100, 8, 8, 5)
        for j in range(len(enemies_x)):
            pyxel.rect(enemies_x[j], 100, 8, 8, 3)
        pyxel.text(0, 0, f'coin: {coin}', 7)
        pyxel.text(0, 10, f'level: {level}', 7)
    else:
        pyxel.text(40,50,'press R to continue',0)

__init__()