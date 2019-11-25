# settings.py
class Settings():
    '''存储《外星人入侵》的所有设置的类'''
    def __init__(self):
        '''初始化游戏设置'''
        self.screen_width = 1200  # 屏幕设置尺寸
        self.screen_height = 800
        self.bg_color = (230,230,230) # 屏幕背景色
        '''飞船的设置'''
        self.ship_speed_factor = 1.5
        self.ship_limit =3

        '''子弹的设置'''
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 6  # 增加编组中子弹最大数量限制

        '''外星人设置'''
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 6
        # fleet_direction 为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1
