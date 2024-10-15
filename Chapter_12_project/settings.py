class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        # 颜色是以RGB值指定的。这种颜色由红色、绿色和蓝色值组成，其中每个值的可能取值范围都为0~255。
        # 颜色值(255, 0, 0)表示红色，(0, 255, 0)表示绿色，而(0, 0,255)表示蓝色。
        # 通过组合不同的RGB值，可创建1600万种颜色。
        # 在颜色值(230, 230, 230)中，红色、蓝色和绿色量相同，它将背景设置为一种浅灰色
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5

        #子弹设置
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
