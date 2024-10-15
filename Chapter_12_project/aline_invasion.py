import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    #初始化背景设置
    pygame.init()
    vijay_settings = Settings()
    #创建一个名为screen的显示窗口，实参（800，600）是一个元组，指定游戏尺寸
    screen = pygame.display.set_mode((vijay_settings.screen_width, vijay_settings.screen_height))
    pygame.display.set_caption("ViJay Invasion")

    ship = Ship(vijay_settings,screen)
    bullets = Group()
    #游戏主循环
    while True:
        #监听键盘和鼠标事件
        gf.check_events(ship)
        ship.update()
        #背景色填充屏幕
        gf.update_screen(vijay_settings, screen, ship, bullets)

run_game()