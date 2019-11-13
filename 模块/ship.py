# ship.py
# 创建一个名为ship的模块，包含Ship类，负责管理飞船的大部分行为
import pygame
class Ship():
    def __init__(self,screen):
        '''初始化飞船并设置其初始位置'''
        self.screen = screen
        # 加载飞船图像并获取其它外接矩形
        self.image = pygame.image.load('C:\Study\Python\Project_外星人入侵\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)