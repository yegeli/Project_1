# settings.py
class Settings():
    '''存储《外星人入侵》的所有设置的类'''
    def __init__(self):
        '''初始化游戏设置'''
        self.screen_width = 1200  # 屏幕设置尺寸
        self.screen_height = 800
        self.bg_color = (230,230,230) # 屏幕背景色
        # 飞船的设置
        self.ship_speed_factor = 1.5

