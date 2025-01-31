import pygame  #pygameをimport
from pygame.locals import*  #pygameの定数をimport(event.type: QUITなど)
import sys  #sysをimport(sys.exit()でゲーム終了)

FPS = 30  #フレームレートを30にする

def __init__():
    global x, screen
    pygame.init()  #pygameを初期化
    screen = pygame.display.set_mode((800, 600))  #画面サイズを横800、縦600にする
    pygame.display.set_caption("tutorial")  #画面のタイトルをtutorialにする
    x = 0
    clock = pygame.time.Clock()  #フレームレートを管理する時計を用意
    while True:  #run(update, draw)のイメージ
        update()
        draw()
        pygame.display.update()  #(while True以降の処理を行い)画面を更新
        for event in pygame.event.get():  #イベント処理
            if event.type == QUIT:  #画面の×ボタンが押されたら
                pygame.quit()  # pygameを終了する(なくても良い?)
                sys.exit()  #プログラムを終了する(これがないと画面の描写などでエラー吐く)
        clock.tick(FPS)  #30FPSで動くように待つ

def update():
    global x
    x = x + 5
    if x > 800:
        x = 0

def draw():
    screen.fill((0, 0, 0))  #画面をカラーコード(000000 -> 黒色)で塗りつぶす
    pygame.draw.rect(screen, (0,255,255), (x,100,60,60))  #screenに、水色の、座標(x,100)に横60縦60ピクセルの四角を描画

__init__()