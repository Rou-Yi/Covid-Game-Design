import pygame
import os
import math, random
from settings import PATH_E
from all_image import *


class Virus:
    def __init__(self, image, name, stride, attack_objects):
        self.type = name
        self.path = PATH_E_D(random.choice([360, 370, 380, 390, 400, 410, 420]))
        self.path_index = 0
        self.move_count = 0
        self.move_back_count = 0
        self.stride = stride*3  # 移動步伐
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.path[self.path_index]
        self.health = 1
        self.attack_range = 60  # 攻擊範圍
        self.attack_object = attack_objects
        self.attack_tower = False
        self.be_attack = 0

    def check_moving(self):
        """
        Check whether virus reaches the cat or virus is at the last point.
        :param:
        :return: boolean
        """
        # Control the move
        moving = True
        if self.path_index == len(self.path) - 1:
            moving = False
        return moving

    def move(self):
        """
        Virus move until reaching the last point.
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

    def retreat_move(self):
        """
        Virus move back when dead.
        :return: none
        """
        x1, y1 = self.rect.center
        x2, y2 = (random.choice([600, 700]), random.choice([200, 100]))
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        max_count = int(distance / self.stride)
        # compute the unit vector
        unit_vector_x = (x2 - x1) / distance
        unit_vector_y = (y2 - y1) / distance
        # compute the movement
        delta_x = unit_vector_x * self.stride * self.move_back_count
        delta_y = unit_vector_y * self.stride * self.move_back_count
        # update the position and counter
        if self.move_back_count < max_count:
            self.rect.center = (x1 + delta_x, y1 + delta_y)
            self.move_back_count += 1
        else:
            return True
        return False

    def attack(self, ally_group):
        """
        Virus attack action.
        :param ally_group: AllyGroup()
        :return cd time: int
        """
        # attack cat
        for cat in ally_group.get():
            dist_cat = abs(self.rect.x - cat.rect.x)
            # if in range, go on an attack, and cause damage
            if dist_cat <= self.attack_range:
                if self.type != cat.attack_object:
                    cat.health = 0
                    return
        # attack tower
        # 病毒走到最後一步就打塔，打到塔就消失
        if self.check_moving() is not True:
            ally_group.tower.health -= 1
            self.attack_tower = True
            self.health = 0
            return

    @property
    def attack_objects(self):
        return self.attack_object

    # 用繼承寫出病毒種類
    @classmethod
    def Blue_Virus(cls, speed):
        blue_virus = cls(BLUE_VIRUS_IMAGE_M, 'blue virus', stride=speed, attack_objects='normal')
        return blue_virus

    @classmethod
    def Black_Virus(cls, speed):
        black_virus = cls(BLACK_VIRUS_IMAGE_M, 'black virus', stride=speed, attack_objects='mask')
        return black_virus

    @classmethod
    def Yellow_Virus(cls, speed):
        yellow_virus = cls(YELLOW_VIRUS_IMAGE_M, 'yellow virus', stride=speed, attack_objects='sanitizer')
        return yellow_virus

    @classmethod
    def Red_Virus(cls, speed):
        red_virus = cls(RED_VIRUS_IMAGE_M, 'red virus', stride=speed, attack_objects='vaccine')
        return red_virus

    @classmethod
    def Orange_Virus(cls, speed):
        orange_virus = cls(ORANGE_VIRUS_IMAGE_M, 'orange virus', stride=speed, attack_objects='alcohol')
        return orange_virus

