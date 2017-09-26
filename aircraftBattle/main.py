#coding=utf-8

import pygame
import time
import random
from pygame.locals import *

# 飞机的基类
class BasePlane(object):
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)
        self.bulletList = []

# 子弹的基类
class BaseBullet(object):
    def __init__(self, screen, x, y, url):
        self.x = x
        self.y = y
        self.screen = screen
        self.image = pygame.image.load(url)

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

class Plane(BasePlane):
    def __init__(self, screen):
        BasePlane.__init__(self, screen, 210, 700, "./img/hero1.png")  # super.__init__()
        # 爆炸效果用的如下属性
        self.hit = False  # 表示是否要爆炸
        self.bomb_list = []  # 用来存储爆炸时需要的图片
        self.__crate_images()  # 调用这个方法向bomb_list中添加图片
        self.image_num = 0  # 用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号

    # 加载图片
    def __crate_images(self):
        self.bomb_list.append(pygame.image.load("./img/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("./img/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("./img/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("./img/hero_blowup_n4.png"))

    # 显示玩家的飞机
    def display(self):
        # 如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_num = 0
                self.image_index += 1
            if self.image_index > 3:
                time.sleep(1)
                exit()  # 调用exit让游戏退出
                # self.image_index = 0
        else:
            self.screen.blit(self.image, (self.x, self.y))

        # 无论是否被命中 都要显示发射出去的子弹
        temp = []
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界 若越界则删除
                temp.append(bullet)

        # 防止跳跃删除
        for i in temp:
            if i in self.bulletList:
                self.bulletList.remove(i)

    # 更改爆炸状态
    def bomb(self):
        self.hit = True

    # 移动
    def move_left(self):
        self.x -= 10
    def move_right(self):
        self.x += 10

    # 开火
    def fire(self):
        self.bulletList.append(Bullet(self.screen, self.x, self.y))

# 敌机的类
class EnemyPlane(BasePlane):
    def __init__(self, screen):
        BasePlane.__init__(self, screen, 0, 0, "./img/enemy0.png")
        self.direction = "right"  # 飞机飞行方向

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bulletList:
            bullet.display()
            bullet.move()

    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x >= 430:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

    def fire(self):
        # 随机产生子弹, 大约就是 range*sleepTime 秒产生一颗子弹
        # 范围变小则产生子弹的概率会增加， 所以需要二次进行子弹数目的增加
        random_num = random.randint(1, 100)
        if random_num == 20 or random_num == 80 or random_num == 50:
            self.bulletList.append(EnemyBullet(self.screen, self.x, self.y))

class Bullet(BaseBullet):
    def __init__(self, screen, x, y):
        BaseBullet.__init__(self, screen, x+40, y-20, "./img/bullet.png")

    def move(self):
        self.y -= 10

    # 判断子弹是否越界
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

# 敌机的子弹类
class EnemyBullet(BaseBullet):
    def __init__(self, screen, x, y):
        BaseBullet.__init__(self, screen, x + 25, y + 40, "./img/bullet1.png")

    def move(self):
        self.y += 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

# 获取案件事件, 这句话之前的按键都获取下来
def key_control(plane):
    for event in pygame.event.get():
        # 点击退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否有按键
        elif event.type == KEYDOWN:
            # 检测按键是否 是a或者left
            # 检测按键是否 是d或者right
            # 如果是则 左右移动5像素
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                plane.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                plane.move_right()
            # 检测按键是否 为空格
            elif event.key == K_SPACE:
                print('space')
                plane.fire()
            elif event.key == K_b:
                print('b')
                plane.bomb()


def main():
    screen = pygame.display.set_mode((480, 852), 0, 32)

    background = pygame.image.load("./img/background.png")
    # airplane = pygame.image.load("./img/hero1.png")
    # 创建一个对象, 并传入一个对象
    plane = Plane(screen)

    # 创建一个敌机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        plane.display()
        enemy.display()
        enemy.move()
        enemy.fire()

        pygame.display.update()

        # 键盘输入
        key_control(plane)
        # 延时,防止老电脑cpu飙升
        time.sleep(0.01)


if __name__ == "__main__":
    main()