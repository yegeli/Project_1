# 模块sys用于退出游戏
import sys
import pygame

def check_events():
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    '''更新屏幕上的图像'''
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    # 调用方法screen.fill()用背景色填充屏幕，这个方法只接受一个实参：一种颜色
    ship.blitme()
    # 让最近绘制的屏幕可见
    pygame.display.flip()