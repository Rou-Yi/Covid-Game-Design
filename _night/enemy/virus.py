import pygame
import os
import math, random
from all_image import *
from sound import virus_attack_soundtrack


class Virus:
    # [一般圖像. 被攻擊圖. 名字. 血量. 攻擊力. 攻擊範圍. 移動步伐. 攻擊cd]
    def __init__(self, image, hit_image, name, health, damage, attack_range, stride, attack_cd):
        self.type = name
        # 使用 random.choice 選擇路線的 y 軸
        self.path = PATH_E(random.choice([360, 370, 380, 390, 400, 410, 420]))
        self.path_index = 0
        self.move_count = 0
        self.move_back_count = 0
        self.back_count = 0
        self.stride = stride  # 移動步伐
        self.hit_image = hit_image  # 被攻擊的圖
        self.normal_image = image  # 一般狀態的圖
        self.image = self.normal_image
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]

        self.health = health
        self.max_health = health  # 血量
        self.damage = damage  # 攻擊力
        self.attack_range = attack_range  # 攻擊範圍
        self.cd_count = attack_cd  # 攻擊 CD
        self.cd_max_count = attack_cd

        self.move_back_permit = False

    def check_moving(self, ally_group):
        """
        Check whether virus reaches the cat or virus is at the last point.
        :param ally_group: AllyGroup()
        :return: boolean
        """
        # Control the move
        moving = True
        for cat in ally_group.get():
            # calculate the distance between cat and virus
            dist = abs(cat.rect.x - self.rect.x)
            if dist <= self.attack_range:
                moving = False  # stop moving
                break
        if self.path_index == len(self.path) - 1:
            moving = False
        return moving

    def move_back(self):
        """被打到的時候要後退"""
        if self.move_back_permit:
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
        Virus move until reaching the last point.
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

    def attack(self, ally_group):
        """
        Virus attack action.
        :param ally_group: AllyGroup()
        :return :
        """
        # 保留 15 幀的攻擊圖片
        if self.cd_count == 15:
            self.image = self.normal_image  # 更新回原本普通圖
        if self.cd_count < self.cd_max_count:
            self.cd_count += 1
        else:
            # attack cat
            for cat in ally_group.get():
                dist_cat = abs(self.rect.x - cat.rect.x)
                # if in range, go on an attack, and cause damage
                if dist_cat <= self.attack_range:
                    cat.health -= self.damage
                    cat.be_attacked()
                    self.cd_count = 0
                    virus_attack_soundtrack()
                    return
            # attack tower
            dist_tw = abs(self.rect.x - ally_group.tower.rect.right)
            if dist_tw <= self.attack_range:
                ally_group.tower.health -= self.damage
                self.cd_count = 0
                virus_attack_soundtrack()
                return
            # if no attack, keep CD count
            self.cd_count = 61

    def be_attacked(self):
        """被打到時，更換圖片，啟動退回機制"""
        self.image = self.hit_image
        self.move_back_permit = True

    # 用繼承寫出病毒種類
    @classmethod
    def Normal_Virus(cls):
        normal_virus = cls(BLUE_VIRUS_IMAGE, BLUE_VIRUS_behitted_IMAGE, 'normal_virus',
                           health=200, damage=20, attack_range=100, stride=1.3, attack_cd=80)
        return normal_virus

    @classmethod
    def Alpha_Virus(cls):
        alpha_virus = cls(BLACK_VIRUS_IMAGE, BLACK_VIRUS_behitted_IMAGE, 'black virus',
                          health=250, damage=50, attack_range=110, stride=1.2, attack_cd=100)
        return alpha_virus

    @classmethod
    def Beta_Virus(cls):
        beta_virus = cls(YELLOW_VIRUS_IMAGE, YELLOW_VIRUS_behitted_IMAGE, 'yellow virus',
                         health=300, damage=70, attack_range=120, stride=1.1, attack_cd=105)
        return beta_virus

    @classmethod
    def Delta_Virus(cls):
        delta_virus = cls(RED_VIRUS_IMAGE, RED_VIRUS_behitted_IMAGE, 'red virus',
                          health=400, damage=90, attack_range=135, stride=1.2, attack_cd=115)
        return delta_virus

    @classmethod
    def Theta_Virus(cls):
        theta_virus = cls(ORANGE_VIRUS_IMAGE, ORANGE_VIRUS_behitted_IMAGE, 'orange virus',
                          health=500, damage=100, attack_range=145, stride=1.3, attack_cd=120)
        return theta_virus



