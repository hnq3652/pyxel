import pyxel

PLAYER_SPEED = 2

def __init__():
    global player_x, player_y
    pyxel.init(160,120)
    pyxel.load('my_resource.pyxres')
    player_x, player_y = 0, 0
    pyxel.run(update, draw)

def update():
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

def draw():
    pyxel.cls(0)
    pyxel.blt(player_x, player_y, 0, 0, 0, 10, 16)

__init__()