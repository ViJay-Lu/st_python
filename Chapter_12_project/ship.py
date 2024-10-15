import pygame

class Ship():
    def __init__(self,vijay_settings,screen):
        #初始化飞船，并设置初始位置
        self.screen = screen
        self.vijay_settings = vijay_settings
        #加载图像并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        #设置图片大小
        self.image = pygame.transform.scale(self.image,(80,80))
        #获取飞船外接矩形
        self.rect = self.image.get_rect()
        #获取屏幕外接矩形
        self.screen_rect = screen.get_rect()

        #将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        #飞船属性center中存储小数
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False



    def update(self):
        """
        if self.moving_right:
            #self.rect.centerx += 1
            self.center_x += self.vijay_settings.ship_speed
        if self.moving_left:
            #self.rect.centerx -= 1
            self.center_x -= self.vijay_settings.ship_speed
        if self.moving_up:
            #self.rect.centery -= 1
            self.center_y -= self.vijay_settings.ship_speed
        if self.moving_down:
            #self.rect.centery += 1
            self.center_y += self.vijay_settings.ship_speed
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center_x += self.vijay_settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.center_x -= self.vijay_settings.ship_speed
        elif self.moving_up and self.rect.centery > self.screen_rect.centery:
            self.center_y -= self.vijay_settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.center_y += self.vijay_settings.ship_speed

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y


    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)