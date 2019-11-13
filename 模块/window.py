#window.py
# 模块sys用于退出游戏
import sys
import pygame
from settings import Settings
def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("小子，你瞅啥啊")
    '''开始游戏的主循环'''
    while True:
        '''监视键盘和鼠标事件'''
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                sys.exit()
        '''每次循环时都重绘屏幕'''
        #调用方法screen.fill()用背景色填充屏幕，这个方法只接受一个实参：一种颜色
        screen.fill(ai_settings.bg_color)
        '''让最近绘制的屏幕可见'''
        pygame.display.flip()
run_game()
