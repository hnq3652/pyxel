import pyxel  #pyxelモジュールをインポートする

PLAYER_SPEED = 2  #プレイヤーのスピードを定数にする

def __init__():  #ゲームの初期設定をする関数を定義する
    global player_x, player_y, enemy_x, enemy_y  #全ての変数をグローバル化
    pyxel.init(160,120)  #ゲーム画面の縦、横の幅を決める
    pyxel.load('my_resource.pyxres')  #絵や音楽のデータを読み込む
    player_x, player_y = 0, 0  #ゲーム開始時の(プレイヤーのx座標,y座標)を(0,0)にする
    enemy_x, enemy_y = 100, 100  #ゲーム開始時の(敵のx座標,y座標)を(100,100)にする
    pyxel.run(update, draw)  #動き(プレイヤーの座標など)の更新と、描画をし続ける

def update():  #動き(プレイヤーの座標など)の更新をする関数を定義する
    global player_x, player_y  #プレイヤーのx座標、y座標をグローバル化
    global enemy_x, enemy_y
    if pyxel.btn(pyxel.KEY_W):  #もしWが押されたら(長押し可能)
        player_y = player_y - PLAYER_SPEED  #プレイヤーのy座標を2減らす(上に2動く)
    elif pyxel.btn(pyxel.KEY_S):
        player_y = player_y + PLAYER_SPEED  #プレイヤーのy座標を2増やす(下に2動く)
    if pyxel.btn(pyxel.KEY_A):
        player_x = player_x - PLAYER_SPEED  #プレイヤーのx座標を2減らす(左に2動く)
    elif pyxel.btn(pyxel.KEY_D):
        player_x = player_x + PLAYER_SPEED  #プレイヤーのx座標を2増やす(右に2動く)
    if player_x > pyxel.width - 10:  #もしx座標が(画面の横幅-10)より大きいなら(画面右側から出たら)
        player_x = pyxel.width - 10  #x座標を画面の右端にする(-10でプレイヤーの大きさ分調整する)
    if player_x < 0:  #もしx座標が0より小さいなら(画面左側から出たら)
        player_x = 0  #x座標を画面の左端にする
    if player_y > pyxel.height - 16:
        player_y = pyxel.height - 16
    if player_y < 0:
        player_y = 0
    enemy_x = enemy_x - 1  #敵は1フレームで右に1移動させる
    if enemy_x < -10:  #左側で見切れたら
        enemy_x = pyxel.width  #右端に戻す

def draw():  #描画をする関数を定義する
    pyxel.cls(0)  #画面を黒色(色番号:0)でリセットする
    pyxel.blt(player_x, player_y, 0, 0, 0, 10, 16)  #x座標がplayer_x(変数),y座標がplayer_yの位置に、パレット0番の0,0から横10、縦16ピクセルの絵を表示する
    pyxel.rect(enemy_x, enemy_y, 10, 10, 3)

__init__()  #ゲームを実行する