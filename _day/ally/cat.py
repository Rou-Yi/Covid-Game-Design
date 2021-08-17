import pygame
import os
import math, random
from settings import PATH_P_D
from color_settings import *
from all_image import *
from sound import cat_attack_soundtrack


class Cats:
    def __init__(self, image, attack_image, name, attack_objects, key_object):
        self.type = name
        self.key_object = key_object
        self.path = PATH_P_D(380)
        self.path_index = 0
        self.move_count = 0
        self.stride = 5  # 移動步伐
        self.normal_image = image
        self.attack_image = attack_image
        self.image = self.normal_image
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.health = 1
        self.attack_range = 120
        self.attack_object = attack_objects
        self.cd_count = 0  # 攻擊 CD
        self.cd_max_count = 15
        self.knocked_down = False

    def check_moving(self, enemy_group):
        """
        Check whether cat reaches the virus or cat is at the last point.
        :param :
        :return: boolean
        """
        # Control the move
        if self.path_index == len(self.path) - 1:  # 走到最後一步停下
            return False
        if enemy_group.is_empty():  # 遊戲贏了開始移動
            return True
        return False

    def move(self):
        """
        Cat moves until reaching the last point.
        :return: none
        """
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
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
        else:
            self.image = self.normal_image  # 更新回原本普通圖
            self.cd_count = 0

        # attack virus
        self.knocked_down = False
        for virus in enemy_group.get():
            dist_en = abs(self.rect.x - virus.rect.x)
            # if in range, go on an attack, and cause damage
            if dist_en <= self.attack_range:
                if self.type == virus.attack_object:
                    virus.health = 0
                    virus.be_attack += 1
                    self.image = self.attack_image
                    cat_attack_soundtrack()
                    if virus.be_attack == 1:
                        self.knocked_down = True
                    return
        # attack tower
        dist_tw = abs(self.rect.x - enemy_group.tower.rect.left)
        if dist_tw <= self.attack_range:
            enemy_group.tower.health = 0
            self.image = self.attack_image
            cat_attack_soundtrack()
            return

    @property
    def attack_objects(self):
        return self.attack_object

    # 用繼承寫出貓咪種類
    @classmethod
    def Normal_Cat(cls):  # 第一種普通貓
        normal_cat = cls(NORMAL_CAT_IMAGE_D, NORMAL_CAT_ATTACK_IMAGE_D, 'normal',
                         attack_objects='blue virus', key_object="key G")
        return normal_cat

    @classmethod
    def Mask_Cat(cls):  # 第二種口罩貓
        mask_cat = cls(MASK_CAT_IMAGE_D, MASK_CAT_ATTACK_IMAGE_D, 'mask',
                       attack_objects='black virus', key_object="key H")
        return mask_cat

    @classmethod
    def Sanitizer(cls):
        sanitizer = cls(SANI_CAT_IMAGE_D, SANI_CAT_ATTACK_IMAGE_D, 'sanitizer',
                        attack_objects='yellow virus', key_object="key J")
        return sanitizer

    @classmethod
    def Alcohol(cls):
        alcohol = cls(ALCOHOL_CAT_IMAGE_D, ALCOHOL_CAT_ATTACK_IMAGE_D, 'alcohol',
                      attack_objects='orange virus', key_object="key K")
        return alcohol

    @classmethod
    def Vaccine(cls):
        vaccine = cls(VACCINE_CAT_IMAGE_D, NORMAL_CAT_ATTACK_IMAGE_D, 'vaccine',
                      attack_objects='red virus', key_object="key L")
        return vaccine

