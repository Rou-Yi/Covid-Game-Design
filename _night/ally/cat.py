import pygame
import os
import math, random
from settings import PATH_P
from all_image import *
from sound import cat_attack_soundtrack


class Cats:
    # [圖像. 攻擊中的圖像. 名字. 血量. 攻擊力. 攻擊範圍. 移動步伐. 召喚消耗, 召喚CD]
    def __init__(self, image, attack_image, name, health, damage, attack_range, stride, cost, attack_cd):
        self.type = name
        self.path = PATH_P(random.choice([360, 370, 380, 390, 400, 410, 420]))
        self.path_index = 0
        self.move_count = 0
        self.move_back_count = 0
        self.back_count = 0
        self.stride = stride  # 移動步伐
        self.normal_image = image
        self.attack_image = attack_image
        self.image = self.normal_image
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]

        self.health = health
        self.max_health = health  # 血量
        self.damage = damage  # 攻擊力
        self.attack_range = attack_range  # 攻擊範圍
        self.cost = cost  # 召喚消耗
        self.cd_count = attack_cd  # 攻擊 CD
        self.cd_max_count = attack_cd
        self.attack_permit = False
        self.move_back_permit = False

    def check_moving(self, enemy_group):
        """
        Check whether cat reaches the virus or cat is at the last point.
        :param enemy_group: EnemyGroup()
        :return: boolean
        """
        # Control the move
        moving = True
        for virus in enemy_group.get():
            # calculate the distance between cat and virus
            dist = abs(virus.rect.x - self.rect.x)
            if dist <= self.attack_range:
                moving = False  # stop moving
                break
        if self.path_index == len(self.path) - 1:
            moving = False
        return moving

    def move_back(self):
        if self.move_back_permit:
            # 被打回到第一步 或是 走到最後一步時
            if (self.path_index == 0) or (self.path_index == len(self.path) - 1):
                self.rect.center = self.path[self.path_index]
            else:
                x1, y1 = self.path[self.path_index]
                x2, y2 = self.path[self.path_index + 1]
                x3, y3 = self.path[self.path_index - 1]
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
                max_count = int(distance / self.stride)
                # compute the unit vector
                unit_vector_x = (x2 - x1) / distance
                unit_vector_y = (y2 - y1) / distance
                # compute the movement
                delta_x = unit_vector_x * self.stride * self.move_back_count
                delta_y = unit_vector_y * self.stride * self.move_back_count

                if self.move_back_count > 0:
                    self.rect.center = (x1 - delta_x, y1 - delta_y)
                    self.move_back_count -= 1
                    if self.move_count > 0:
                        self.move_count -= 1
                else:
                    distance = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
                    max_count = int(distance / self.stride)
                    self.move_back_count = max_count
                    self.rect.center = self.path[self.path_index]
                    self.path_index -= 1
                    if self.path_index < 0:
                        self.path_index = 0

                self.back_count += 1  # 計算退後的步數
                if self.back_count > 30:
                    self.move_back_permit = False
                    self.back_count = 0
                    self.move_back_count = 0

    def move(self):
        """
        Cat moves until reaching the last point.
        :return: none
        """
        if self.move_back_permit is not True:
            x1, y1 = self.path[self.path_index]
            x2, y2 = self.path[self.path_index + 1]
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            max_count = int(distance / self.stride)
            # compute the unit vector
            unit_vector_x = (x2 - x1) / distance
            unit_vector_y = (y2 - y1) / distance
            # compute the movement
            delta_x = unit_vector_x * self.stride * self.move_count
            delta_y = unit_vector_y * self.stride * self.move_count
            # update the position and counter
            if self.move_count < max_count:
                self.rect.center = (x1 + delta_x, y1 + delta_y)
                self.move_count += 1
            else:
                self.move_count = 0
                self.path_index += 1
                self.rect.center = self.path[self.path_index]

    def attack(self, enemy_group):
        """
        Cat attack action.
        :param enemy_group: EnemyGroup
        :return cd time: int
        """
        # 保留 15 幀的攻擊圖片
        if self.cd_count == 15:
            self.image = self.normal_image  # 更新回原本普通圖
        # 當CD滿足時，執行攻擊
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
        else:
            # attack virus
            for virus in enemy_group.get():
                dist_virus = abs(self.rect.x - virus.rect.x)
                # if in range, go on an attack, and cause damage
                if dist_virus <= self.attack_range:
                    virus.health -= self.damage
                    virus.be_attacked()
                    self.cd_count = 0
                    cat_attack_soundtrack()
                    self.image = self.attack_image
                    return
            # attack tower
            dist_tw = abs(self.rect.x - enemy_group.tower.rect.left)
            if dist_tw <= self.attack_range:
                enemy_group.tower.health -= self.damage
                self.cd_count = 0
                cat_attack_soundtrack()
                self.image = self.attack_image
                return
            # if no attack, keep CD count
            self.cd_count = 61

    def be_attacked(self):
        #self.image = self.hit_image
        self.move_back_permit = True

    @property
    def get_cost(self):
        return self.cost

    # 用繼承寫出貓咪種類
    @classmethod
    def Normal_Cat(cls):  # 第一種普通貓
        normal_cat = cls(NORMAL_CAT_IMAGE, NORMAL_CAT_ATTACK_IMAGE, 'normal',
                         health=100, damage=20, attack_range=100, stride=1.5, cost=15, attack_cd=75)
        return normal_cat

    @classmethod
    def Mask_Cat(cls):  # 第二種口罩貓
        mask_cat = cls(MASK_CAT_IMAGE, MASK_CAT_ATTACK_IMAGE, 'mask',
                       health=200, damage=50, attack_range=120, stride=1, cost=25, attack_cd=90)
        return mask_cat

    @classmethod
    def Sanitizer(cls):
        sanitizer = cls(SANI_CAT_IMAGE, SANI_CAT_ATTACK_IMAGE, 'sanitizer',
                        health=300, damage=70, attack_range=130, stride=1, cost=30, attack_cd=110)
        return sanitizer

    @classmethod
    def Alcohol(cls):
        alcohol = cls(ALCOHOL_CAT_IMAGE, ALCOHOL_CAT_ATTACK_IMAGE, 'alcohol',
                      health=400, damage=80, attack_range=140, stride=1.2, cost=40, attack_cd=120)
        return alcohol

    @classmethod
    def Vaccine(cls):
        vaccine = cls(VACCINE_CAT_IMAGE, VACCINE_CAT_ATTACK_IMAGE, 'vaccine',
                      health=500, damage=110, attack_range=150, stride=1.3, cost=50, attack_cd=130)
        return vaccine



