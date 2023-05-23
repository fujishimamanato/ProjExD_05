import sys
import time
import random

import pygame as pg

# 色の数値の設定
white = (255,255,255)
black = (0,0,0)
green = (0,150,0)
red = (255,0,0)
blue = (0,0,255)
light_blue = (147,251,253)
width = 1600 # ディスプレイの横の長さ
height = 900 # ディスプレイの縦の長さ
goalheight = 50 # ゴールの範囲

def check_bound(area: pg.Rect, obj: pg.Rect) -> tuple[bool, bool]:
    yoko, tate = True, True
    if obj.left < area.left or area.right < obj.right:  # 横方向のはみ出し判定
        yoko = False
    if obj.top < area.top or area.bottom < obj.bottom:  # 縦方向のはみ出し判定
        tate = False
    return yoko, tate
class playerlect: # パドルに関するクラス
    # 1パターン目の押下キーと移動量の辞書
    _alfa = {
        pg.K_w: (0, -1),
        pg.K_s: (0, +1),
        pg.K_a: (-1, 0),
        pg.K_d: (+1, 0),
    }
    # 2パターン目の押下キーと移動量の辞書
    _delta = {
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0),
    }
    

    def __init__(self, xy: tuple[int,int], zw: tuple[int,int]): 
        self._img1 = pg.transform.rotozoom(pg.image.load(f"ex05/redpad.png"),0, 2.0)
        self._img2 = pg.transform.rotozoom(pg.image.load(f"ex05/bluepad.png"),0, 2.0)
        self._rct1 = self._img1.get_rect()
        self._rct2 = self._img2.get_rect()
        self._rct1.center = xy
        self._rct2.center = zw


    def update(self,key_lst: list[bool], screen: pg.Surface):
        for k,mv in __class__._delta.items():
            if key_lst[k]:
                self._rct1.move_ip(mv)
        
        for k,mv in __class__._alfa.items():
            if key_lst[k]:
                self._rct2.move_ip(mv)

        screen.blit(self._img1,self._rct1)
        screen.blit(self._img2,self._rct2)

class ball: # ディスクに関するクラス
    _dires = [-1, 0, +1]
    def __init__(self):
        self._img = pg.image.load(f"ex05/disc.png")
        self._rct = self._img.get_rect()
        self._rct.center = width/2,height/2
        self._vx, self._vy = random.choice(ball._dires), random.choice(ball._dires)
        
    def update(self,screen: pg.Surface):
        yoko,tate = check_bound(screen.get_rect(), self._rct)
        if not yoko:
            self._vx *= -1
        if not tate:
            self._vy *= -1
        self._rct.move_ip(self._vx, self._vy)
        screen.blit(self._img,self._rct)

def main():
    pg.display.set_caption("Air-hockey")
    screen = pg.display.set_mode((1600,900))
    pl1 = playerlect((width-300,height/2),(300,height/2))
    disc = ball()
    clock = pg.time.Clock()
    

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.fill((0,0,0))

        # ディスプレイの周りに表示する線に関するプログラム
        pg.draw.line(screen, blue,(0,0), (screen.get_width()/2 - 5,0) ,20)
        pg.draw.line(screen, blue,(0,screen.get_height()), (screen.get_width()/2 - 5,screen.get_height()) ,20)
        pg.draw.line(screen, red, (screen.get_width()/2+5,0), (screen.get_width() ,0) ,20)
        pg.draw.line(screen, red, (screen.get_width()/2 + 5,screen.get_height()) , (screen.get_width(),screen.get_height()) ,20)
        pg.draw.line(screen,white,(width/2,0),(width/2,height),5)
        pg.draw.line(screen, blue, (0,0), (0,screen.get_height()/2-goalheight) ,5)
        pg.draw.line(screen, blue, (0,screen.get_height()/2 + goalheight), (0,screen.get_height()) ,5)
        pg.draw.line(screen, red, (screen.get_width(),0), (screen.get_width(),screen.get_height()/2-goalheight) ,5)
        pg.draw.line(screen, red, (screen.get_width(),screen.get_height()/2 + goalheight), (screen.get_width(),screen.get_height()) ,5)



        key_lst = pg.key.get_pressed()
        
        pl1.update(key_lst,screen)
        disc.update(screen)

        pg.display.update()
        clock.tick(1000)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()