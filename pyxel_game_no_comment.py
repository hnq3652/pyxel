import pyxel

PLAYER_SPEED = 2

def __init__():
    global player_x, player_y, enemy_x, enemy_y, player_alive
    pyxel.init(160,120)
    pyxel.load('my_resource.pyxres')
    player_x, player_y = 0, 0
    enemy_x, enemy_y = 100, 100
    player_alive = True
    pyxel.run(update, draw)

def update():
    update_player()
    update_enemy()
    check_collision()

def update_player():
    global player_x, player_y
    if pyxel.btn(pyxel.KEY_W):
        player_y = player_y - PLAYER_SPEED
    elif pyxel.btn(pyxel.KEY_S):
        player_y = player_y + PLAYER_SPEED
    if pyxel.btn(pyxel.KEY_A):
        player_x = player_x - PLAYER_SPEED
    elif pyxel.btn(pyxel.KEY_D):
        player_x = player_x + PLAYER_SPEED
    if player_x > pyxel.width - 10:
        player_x = pyxel.width - 10
    if player_x < 0:
        player_x = 0
    if player_y > pyxel.height - 16:
        player_y = pyxel.height - 16
    if player_y < 0:
        player_y = 0

def update_enemy():
    global enemy_x, enemy_y
    enemy_x = enemy_x - 1
    if enemy_x < -10:
        enemy_x = pyxel.width

def check_collision():
    global player_alive
    if enemy_x-10 < player_x < enemy_x+8 and enemy_y-16 < player_y < enemy_y+8:
        player_alive = False

def draw():
    pyxel.cls(0)
    if player_alive:
        pyxel.blt(player_x, player_y, 0, 0, 0, 10, 16)
    else:
        pyxel.blt(player_x, player_y, 0, 0, 0, 10, -16)
    pyxel.rect(enemy_x, enemy_y, 8, 8, 3)

__init__()